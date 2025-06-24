# Real GDP Analysis for Nigeria

This project analyzes the Real Gross Domestic Product (GDP) of Nigeria over time using data from a CSV file sourced from the Federal Reserve Economic Data (FRED). The analysis includes data loading, preprocessing, exploration, and visualization of year-over-year GDP growth rates using Python libraries such as pandas, seaborn, and matplotlib within a Jupyter Notebook environment. The project highlights key trends, including the impact of the COVID-19 pandemic period (2020-2021), marked on the visualization.

## Project Overview

- **Objective**: Analyze and visualize Nigeria's Real GDP growth rate from 1950 to 2019 to identify economic trends and the impact of significant events like the COVID-19 pandemic.
- **Data Source**: `nigeria_real_gdp_fred.csv`, loaded from a local file in `/Users/user/Downloads/`.
- **Tools**: Python 3.12.7, pandas, seaborn, matplotlib, Jupyter Notebook.
- **Output**: A bar chart showing year-over-year GDP growth rates with a shaded region for the 2020-2021 pandemic period.

## Setup Instructions

### Prerequisites
- Install required Python libraries:
  ```bash
  pip install seaborn matplotlib pandas requests beautifulsoup4 warnings
  ```
- Ensure Python 3.12.7 or a compatible version is installed.
- Download the dataset `nigeria_real_gdp_fred.csv` and place it in `/Users/user/Downloads/` (update the path as needed).
- Use a Jupyter Notebook environment (e.g., JupyterLab or VS Code with Jupyter support).

### Environment Setup
- No web scraping or external drivers are required beyond the initial CSV file load.
- Adjust the file path in the `pd.read_csv()` call if the dataset is stored elsewhere.

## Project Steps

### 1. Importing Libraries
- **Task**: Load necessary Python libraries for data analysis and visualization.
- **Implementation**:
  - Imported `seaborn` and `matplotlib.pyplot` for plotting.
  - Imported `requests` and `BeautifulSoup` (though unused in this version).
  - Imported `pandas` for data manipulation.
  - Imported `warnings` to suppress FutureWarning messages with `warnings.simplefilter(action='ignore', category=FutureWarning)` for cleaner output.
- **Outcome**: Established a foundation for data processing and visualization.

### 2. Loading and Preprocessing Data
- **Task**: Load the CSV file containing Nigeria's Real GDP data and preprocess it by renaming columns.
- **Implementation**:
  - Used `pd.read_csv('/Users/user/Downloads/nigeria_real_gdp_fred.csv')` to load the data.
  - Renamed columns from `observation_date` to `Date` and `RGDPNANGA666NRUG` to `Real_GDP` using `gdp.rename(columns={...})`.
  - Previewed the first five rows with `print(gdp.head())` to confirm the structure.
- **Outcome**: Loaded a DataFrame with 70 rows and 2 columns (`Date` and `Real_GDP`), starting from 1950-01-01 with `Real_GDP` at 78,915.1875 and ending at 2019-01-01 with 1,006,237.

### 3. Data Exploration
- **Task**: Explore the dataset's structure, content, and statistical summary.
- **Implementation**:
  - Displayed the full DataFrame with `gdp` to verify all 70 rows, showing `Real_GDP` growth from 78,915.1875 (1950) to 1,006,237 (2019).
  - Attempted `gdp.info` (note: this was a method call error, intended as `gdp.info()` for metadata).
  - Generated descriptive statistics with `gdp.describe()`, showing `Real_GDP` mean of 354,717.4, min of 78,915.1875, max of 1,006,237, and quartiles.
  - Checked for missing values with `gdp.isnull().sum()`, confirming no null entries.
  - Verified DataFrame shape with `gdp.shape`, confirming 70 rows and 2 columns.
- **Outcome**: Confirmed a complete dataset with no missing values, providing a range of `Real_GDP` from 78,915.1875 to 1,006,237 over 70 years.

### 4. Visualization
- **Task**: Create a bar chart to visualize year-over-year GDP growth rates.
- **Implementation**:
  - Note: The provided code references `YoY_Growth`, which is not present in the DataFrame. Assuming a preprocessing step was intended but omitted, this summary infers the need for a year-over-year growth calculation (e.g., `gdp['YoY_Growth'] = gdp['Real_GDP'].pct_change() * 100`).
  - Created a figure with `plt.figure(figsize=(12, 6))` for a 12x6 inch plot.
  - Plotted a bar chart with `plt.bar(gdp['Date'], gdp['YoY_Growth'], color='seagreen')`.
  - Added a horizontal line at zero with `plt.axhline(0, color='black', linestyle='--')` for reference.
  - Shaded the 2020-2021 pandemic period with `plt.axvspan(pd.to_datetime('2020-01-01'), pd.to_datetime('2021-12-31'), color='red', alpha=0.15)`.
  - Set titles and labels with `plt.title('Year-over-Year GDP Growth Rate (%)')`, `plt.xlabel('Date')`, and `plt.ylabel('Growth Rate (%)')`.
  - Added a grid with `plt.grid(axis='y')` and displayed the plot with `plt.show()`.
- **Outcome**: A bar chart showing GDP growth rates over time, with a red shaded area highlighting the 2020-2021 period, though actual growth data requires the missing `YoY_Growth` calculation.

## How to Run the Project

1. **Clone or Download the Repository**:
   - Save the `Real_GDP.ipynb` notebook in your working directory.

2. **Set Up Dataset**:
   - Download `nigeria_real_gdp_fred.csv` and place it in `/Users/user/Downloads/` (update the path as needed).

3. **Execute the Notebook**:
   - Open the notebook in a Jupyter environment.
   - Run all cells sequentially:
     - Cell 1: Imports libraries.
     - Cell 2: Loads and preprocesses the data.
     - Cell 3: Explores the data (fix `gdp.info` to `gdp.info()`).
     - Cell 4: Visualizes the GDP growth (add `YoY_Growth` calculation if needed).
   - Note: Add `gdp['YoY_Growth'] = gdp['Real_GDP'].pct_change() * 100` before visualization to compute growth rates.

4. **View Outputs**:
   - `gdp.head()` shows the first five rows (1950-1954).
   - `gdp.describe()` provides statistical summary.
   - The bar chart displays growth rates (once calculated).

## Results and Insights
- **Data Structure**: The dataset spans 1950 to 2019 with 70 annual entries, showing `Real_GDP` increasing from 78,915.1875 to 1,006,237.
- **Statistical Insights**: Mean `Real_GDP` is 354,717.4, with a standard deviation of 268,660.3, indicating significant growth variability.
- **Visualization Insights**: The intended bar chart would show growth trends, with the 2020-2021 shaded area suggesting a potential economic downturn due to the pandemic (data beyond 2019 is unavailable).
- **Limitations**: The `YoY_Growth` column is missing, requiring calculation. The dataset ends in 2019, limiting pandemic analysis to inference.

## Future Improvements
- **Growth Calculation**: Add `gdp['YoY_Growth'] = gdp['Real_GDP'].pct_change() * 100` to compute and visualize growth rates accurately.
- **Data Extension**: Incorporate post-2019 data to analyze the pandemic's full impact.
- **Additional Visualizations**: Add a line plot for `Real_GDP` over time or a box plot for growth distribution.
- **Error Handling**: Include try-except blocks for file loading to handle missing or corrupted data.

## License
This project is for educational purposes. Feel free to modify and use it under a permissive license (e.g., MIT).

## Acknowledgments
- Data sourced from the FRED dataset (`nigeria_real_gdp_fred.csv`).