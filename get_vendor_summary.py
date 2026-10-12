
import sqlite3
import logging
from pathlib import Path

import pandas as pd
from ingestion_db import ingest_db


# Project paths
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "inventory.db"
LOG_DIR = BASE_DIR / "logs"

# Create the logs folder if it does not exist
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=str(LOG_DIR / "get_vendor_summary.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)


def create_vendor_summary(conn):
    """Merge vendor, purchase, sales, and freight data."""

    vendor_sales_summary = pd.read_sql_query(
        """
        WITH FreightSummary AS (
            SELECT
                VendorNumber,
                SUM(Freight) AS FreightCost
            FROM vendor_invoice
            GROUP BY VendorNumber
        ),

        PurchaseSummary AS (
            SELECT
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price AS ActualPrice,
                pp.Volume,
                SUM(p.Quantity) AS TotalPurchaseQuantity,
                SUM(p.Dollars) AS TotalPurchaseDollars
            FROM purchases p
            JOIN purchase_prices pp
                ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price,
                pp.Volume
        ),

        SalesSummary AS (
            SELECT
                VendorNo,
                Brand,
                SUM(SalesQuantity) AS TotalSalesQuantity,
                SUM(SalesDollars) AS TotalSalesDollars,
                SUM(SalesPrice) AS TotalSalesPrice,
                SUM(ExciseTax) AS TotalExciseTax
            FROM sales
            GROUP BY VendorNo, Brand
        )

        SELECT
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume,
            ps.TotalPurchaseQuantity,
            ps.TotalPurchaseDollars,
            ss.TotalSalesQuantity,
            ss.TotalSalesDollars,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss
            ON ps.VendorNumber = ss.VendorNo
            AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC
        """,
        conn,
    )

    return vendor_sales_summary


def clean_data(df):
    """Clean data and create vendor performance metrics."""

    # Work on a copy instead of modifying the original DataFrame
    df = df.copy()

    # Convert Volume to numeric safely
    df["Volume"] = pd.to_numeric(
        df["Volume"], errors="coerce"
    )

    # Fill missing values
    df = df.fillna(0)

    # Remove unnecessary spaces from text columns
    for column in ["VendorName", "Description"]:
        df[column] = df[column].astype(str).str.strip()

    # Gross profit based on sales less purchase dollars
    df["GrossProfit"] = (
        df["TotalSalesDollars"]
        - df["TotalPurchaseDollars"]
    )

    # Avoid division by zero
    sales = df["TotalSalesDollars"].where(
        df["TotalSalesDollars"] != 0
    )

    purchases = df["TotalPurchaseDollars"].where(
        df["TotalPurchaseDollars"] != 0
    )

    purchase_quantity = df["TotalPurchaseQuantity"].where(
        df["TotalPurchaseQuantity"] != 0
    )

    # Profit margin as a percentage
    df["ProfitMargin"] = (
        df["GrossProfit"].div(sales) * 100
    )

    # Sales quantity relative to purchase quantity
    df["StockTurnover"] = (
        df["TotalSalesQuantity"].div(purchase_quantity)
    )

    # Sales dollars relative to purchase dollars
    df["SalesToPurchaseRatio"] = (
        df["TotalSalesDollars"].div(purchases)
    )

    # Replace undefined or infinite calculated values with zero
    metric_columns = [
        "ProfitMargin",
        "StockTurnover",
        "SalesToPurchaseRatio",
    ]

    df[metric_columns] = (
        df[metric_columns]
        .replace([float("inf"), float("-inf")], float("nan"))
        .fillna(0)
    )

    return df


if __name__ == "__main__":

    logging.info("Creating vendor summary table...")

    try:
        with sqlite3.connect(DB_PATH) as conn:

            summary_df = create_vendor_summary(conn)
            logging.info(
                "Summary created: %s rows, %s columns",
                *summary_df.shape,
            )

            logging.info("Cleaning vendor summary data...")
            clean_df = clean_data(summary_df)

            logging.info(
                "Cleaned data: %s rows, %s columns",
                *clean_df.shape,
            )

            logging.info("Saving vendor summary table...")

            ingest_db(
                clean_df,
                "vendor_sales_summary",
                conn,
            )

            logging.info("Vendor summary process completed.")

    except Exception:
        logging.exception("Vendor summary process failed.")
        raise
