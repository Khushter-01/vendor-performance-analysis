# Vendor Performance Analysis

## Project Overview

This project analyzes vendor and inventory data to understand sales performance, purchasing patterns, profitability, and inventory efficiency. The objective is to identify high-performing vendors, evaluate purchasing contributions, and generate insights that can support better business decisions.

The project uses Python, SQL, Pandas, and Power BI to process data, perform analysis, and present findings through an interactive dashboard.

## Business Objectives

- Analyze vendor-wise sales and purchase performance.
- Identify vendors contributing the most to total purchases and sales.
- Evaluate gross profit and profit margins across vendors and brands.
- Examine inventory movement using stock turnover and sales-to-purchase ratios.
- Identify opportunities to improve purchasing decisions and inventory management.

## Tools and Technologies

- **Python:** Data processing and analysis
- **Pandas and NumPy:** Data cleaning and transformation
- **SQL and SQLite:** Data storage, querying, and summary table creation
- **Matplotlib and Seaborn:** Exploratory data analysis and visualization
- **SciPy:** Statistical analysis
- **Power BI:** Interactive dashboard development
- **Jupyter Notebook:** Analysis and documentation

## Project Workflow

1. **Data Preparation:** Organized the source datasets for analysis.
2. **Database Management:** Stored the datasets in a database and used SQL queries to combine relevant information.
3. **Data Cleaning:** Handled data quality issues and prepared the data for analysis.
4. **Exploratory Data Analysis:** Examined sales, purchases, vendor contributions, and profitability.
5. **Vendor Performance Analysis:** Calculated business metrics such as gross profit, profit margin, stock turnover, and sales-to-purchase ratio.
6. **Dashboard Development:** Presented key performance indicators and vendor-level insights in Power BI.

## Dashboard

The Power BI dashboard summarizes vendor sales, purchases, profitability, and inventory-related metrics.

Add a screenshot of the completed dashboard to the `dashboard` folder and display it here:

`![Vendor Performance Dashboard](dashboard/dashboard.png)`

## Key Analysis Areas

- Vendor purchase and sales contribution
- Sales and purchase value comparison
- Brand-level profitability
- Gross profit and profit margin
- Stock turnover and inventory efficiency
- Unsold inventory and purchasing opportunities

## Repository Structure

```text
vendor-performance-analysis/
├── README.md
├── .gitignore
├── requirements.txt
├── notebooks/
├── scripts/
├── dashboard/
│   ├── vendor_performance.pbix
│   └── dashboard.png
└── data/
    └── README.md
```

## How to Run the Project

1. Clone or download this repository.
2. Install the required Python packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Download the source datasets using the instructions in `data/README.md`.
4. Configure the database and data paths as required by the scripts.
5. Run the notebooks in sequence to explore the data and perform the analysis.
6. Open the Power BI file to explore the dashboard.

## Project Outcomes

This project demonstrates a complete data analysis workflow, from data preparation and SQL-based analysis to business metric calculation and dashboard reporting. It applies analytical techniques to vendor performance and inventory management problems.

## Author

Data Analyst Portfolio Project

Technologies: Python, SQL, Pandas, SQLite, SciPy, and Power BI