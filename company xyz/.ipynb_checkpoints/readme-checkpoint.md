Below is a detailed summary of the project converted into a README file format. This README explains everything done so far, including data loading, preprocessing, analysis, and visualizations, based on the conversations and code provided.

---

# Sales Data Analysis Project for Company XYZ

This project involves analyzing sales data from three supermarket branches of Company XYZ (Abuja, Lagos, and Port Harcourt) to derive actionable insights. The analysis is performed using Python, with libraries such as `pandas` for data manipulation, `seaborn` and `matplotlib` for visualizations, and basic file handling with `glob` and `os`. The goal is to understand sales trends, customer behavior, and financial performance across the branches.

## Project Overview

- **Objective**: Analyze sales data to identify patterns in customer purchases, peak sales times, payment preferences, and profitability by branch and product line.
- **Data Sources**: Three CSV files (`Abuja_Branch.csv`, `Lagos_Branch.csv`, `PortHarcourt_Branch.csv`) containing transaction details.
- **Tools**: Python 3.x, pandas, seaborn, matplotlib.
- **Output**: A combined dataset (`combined_sales_data.csv`) and various visualizations to support business decisions.

## Setup Instructions

### Prerequisites
- Install required Python libraries:
  ```bash
  pip install pandas seaborn matplotlib
  ```
- Ensure Python 3.x is installed on your system.

### Data Preparation
1. **Locate CSV Files**:
   - Obtain the three CSV files (`Abuja_Branch.csv`, `Lagos_Branch.csv`, `PortHarcourt_Branch.csv`).
   - Place them in the same directory as the script (`sales_analysis.py`) or note their full paths (e.g., `C:/Users/YourName/Data/Abuja_Branch.csv`).

2. **Verify File Structure**:
   - Each CSV should contain columns such as `Invoice ID`, `Branch`, `City`, `Customer type`, `Gender`, `Product line`, `Unit price`, `Quantity`, `Tax 5%`, `Total`, `Date`, `Time`, `Payment`, `cogs`, `gross margin percentage`, `gross income`, and `Rating`.

## Project Steps

### 1. Loading Datasets
- **Task**: Combine data from the three branch CSV files into a single dataset.
- **Implementation**:
  - Used `glob.glob("*.csv")` to automatically detect all CSV files in the directory (or explicitly listed files like `["Abuja_Branch.csv", "Lagos_Branch.csv", "PortHarcourt_Branch.csv"]`).
  - Read each file into a pandas DataFrame using a list comprehension: `[pd.read_csv(file) for file in file_list]`.
  - Concatenated the DataFrames into `combined_df` using `pd.concat(df_list, ignore_index=True)` to reset the index.
  - Saved the combined data to `combined_sales_data.csv` with `combined_df.to_csv("combined_sales_data.csv", index=False)` to exclude the index column.
- **Outcome**: A unified dataset ready for analysis, with all transactions from the three branches merged.

### 2. Data Exploration
- **Task**: Understand the structure and statistics of the combined dataset.
- **Implementation**:
  - Printed the first few rows with `combined_df.head()`.
  - Checked the shape (rows, columns) and column names with `combined_df.shape` and `combined_df.columns.tolist()`.
  - Generated a statistical summary with `combined_df.describe()`, revealing an average unit price of ~N18,000, an average quantity of 5 items per transaction, and a total sales value averaging N300,000 with a 4.76% gross margin.
  - Identified missing values with `combined_df.isnull().sum()` and confirmed data types with `combined_df.info()`.
- **Outcome**: Insights into data distribution, including a wide price range (N1,500 to N35,000) and robust sales volume.

### 3. DateTime Feature Processing
- **Task**: Convert and extract meaningful time-based features from `Date` and `Time` columns.
- **Implementation**:
  - Converted `Date` to datetime format with `pd.to_datetime(combined_df['Date'])`.
  - Converted `Time` to time format with `pd.to_datetime(combined_df['Time'], format='%H:%M').dt.time`.
  - Extracted `Day`, `Month`, `Year`, and `Hour` as new columns using `.dt` accessor methods.
  - Printed unique hours (`combined_df['Hour'].unique()`) to identify sales time ranges.
- **Outcome**: Enabled time-based analysis, such as hourly sales trends.

### 4. Categorical Data Analysis
- **Task**: Explore unique values and counts in categorical columns.
- **Implementation**:
  - Defined categorical columns (`Customer type`, `Gender`, `Product line`, `Payment`).
  - Used `combined_df[col].unique()` and `combined_df[col].value_counts()` to list and count unique values for each.
- **Outcome**: Identified diversity in customer types (Member, Normal), genders, product lines (e.g., Food and beverages), and payment methods (Card, Cash).

### 5. Aggregation with GroupBy
- **Task**: Aggregate data by city to analyze financial metrics.
- **Implementation**:
  - Grouped by `City` and aggregated `Gross income`, `Unit Price`, and `Quantity` using `combined_df.groupby('City').agg()` with `sum` and `mean`.
- **Outcome**: Revealed Abuja as the most profitable city with a total gross income of ~N6,000,000.

### 6. Data Visualization
- **Task**: Create visualizations to represent key findings.
- **Initial Visualizations**:
  - **Sales Records by Branch**: Bar plot of transaction counts per branch.
  - **Most Used Payment Method**: Bar plot of payment method frequencies.
  - **Highest and Lowest Sold Product Lines**: Bar plot of transaction counts by product line.
  - **Payment Channels by Product Line**: Stacked bar plot of payment methods per product line.
- **Additional Visualizations**:
  - **Total Gross Income by City**: Bar plot showing city-wise gross income.
  - **Customer Rating Distribution by Product Line**: Box plot of ratings per product line.
  - **Total Quantity Sold by Gender and Product Line**: Stacked bar plot of quantities by gender.
  - **Number of Transactions by Hour**: Line plot of hourly transaction counts.
  - **Payment Method Distribution by Customer Type**: Pie charts for member vs. normal customers.
  - **Total Sales by Month and Product Line**: Heatmap of sales totals.

## How to Run the Project

1. **Clone or Download the Repository**:
   - Save the `sales_analysis.py` script and CSV files in the same directory.

2. **Execute the Script**:
   - Run the script using:
     ```bash
     python sales_analysis.py
     ```
   - Alternatively, use a Jupyter Notebook environment and execute cell by cell.

3. **View Outputs**:
   - Check the directory for `combined_sales_data.csv`.
   - Visualizations will display in separate windows or notebook cells.

## Results and Insights
- **Financial Performance**: Abuja leads in gross income, suggesting a focus on expanding there.
- **Customer Behavior**: Diverse product line purchases with consistent 4.76% margins indicate stable profitability.
- **Peak Times**: Hourly trends can guide staffing decisions.
- **Payment Preferences**: Insights into Card vs. Cash usage by customer type can inform payment system upgrades.

## Future Improvements
- Add statistical tests (e.g., t-tests) to compare city performance.
- Include predictive modeling for sales forecasting.
- Expand data with more branches or time periods.

## License
This project is for educational purposes. Feel free to modify and use it under a permissive license (e.g., MIT).

## Acknowledgments
- Data inspired by Company XYZ's supermarket operations.

---

This README encapsulates all steps, from data loading to visualization, and provides a clear guide for replication. 