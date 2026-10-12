# Dataset Information

## Overview

This folder is used to organize the datasets required for the Vendor Performance Analysis project.

The source data contains information related to inventory, purchases, sales, vendor invoices, and product pricing. These datasets are used to analyze vendor contributions, purchasing costs, sales performance, and profitability.

## Data Files

The analysis uses the following source datasets:

- `begin_inventory.csv` — Beginning inventory information
- `end_inventory.csv` — Ending inventory information
- `purchase_prices.csv` — Product and purchase price information
- `purchases.csv` — Purchase transaction data
- `sales.csv` — Sales transaction data
- `vendor_invoice.csv` — Vendor invoice and freight information

The exact columns and contents should be verified against the original source files.

## Data Availability

Raw CSV files and local database files are excluded from the public repository to avoid unnecessary repository size and to keep the repository focused on the analysis code and documentation.

To reproduce the analysis:

1. Obtain the original datasets from the source used for this project.
2. Place the required CSV files in this `data` folder.
3. Check that the filenames match those expected by the scripts and notebooks.
4. Follow the project README to configure the database and run the analysis.

**Original dataset source:** Add the verified source name and download URL here before publishing.

## Notes

The datasets are used for educational and portfolio purposes. Data quality, missing values, data types, and consistency should be checked before analysis. Do not upload confidential, restricted, or personally identifiable information.