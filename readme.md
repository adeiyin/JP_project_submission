# COVID-19 Vulnerability Analysis Project

## Overview

This project involves analyzing COVID-19 data for Nigeria, specifically focusing on integrating and visualizing data from the Nigeria Community Vulnerability Index (CVI) and pandemic-related metrics extracted from an online source. The project is implemented in a Jupyter Notebook environment (`ncdc.ipynb`) using Python, leveraging libraries such as `pandas`, `seaborn`, `matplotlib`, `requests`, `BeautifulSoup`, and `selenium` for data handling, web scraping, and visualization. Below is a comprehensive explanation of the steps undertaken.

## Project Details

### 1. Setup and Imports
- **Libraries Imported:**
  - `seaborn` and `matplotlib.pyplot` for data visualization.
  - `requests` and `BeautifulSoup` for initial web scraping attempts.
  - `pandas` for data manipulation and analysis.
  - `warnings` to suppress FutureWarning messages for cleaner output.
- **Purpose:** These imports set the foundation for fetching data from the web, processing it into a DataFrame, and creating visualizations to explore relationships between variables.

### 2. Installation of Additional Libraries
- **Action:** The `html5lib` library was installed using `!pip install html5lib` to enhance HTML parsing capabilities.
- **Purpose:** This was likely intended to support more robust parsing of web content, though it wasn't directly utilized in the subsequent scraping steps.

### 3. Initial Web Scraping Attempt
- **Action:** 
  - A request was made to the URL `https://pmc.ncbi.nlm.nih.gov/articles/PMC8548039/` using `requests.get()`.
  - The response was parsed with `BeautifulSoup` using the `"html.parser"`.
  - The first 3000 characters of the parsed HTML were printed with `soup.prettify()[:3000]`.
- **Outcome:** The result indicated a "403 Forbidden" error, suggesting that the webpage blocked direct access or required authentication/javascript rendering that `requests` couldn't handle.
- **Purpose:** This step aimed to extract table data (likely the COVID-19 metrics) directly from the article, but the approach failed due to access restrictions.

### 4. Installation of Selenium
- **Action:** The `selenium` library was installed with `pip install selenium` to enable browser automation for scraping dynamic content.
- **Purpose:** Selenium was introduced to overcome the limitations of `requests` by rendering the webpage in a browser (e.g., Chrome) and accessing the full content, including JavaScript-generated tables.

### 5. Data Extraction Using Selenium
- **Action:**
  - A `webdriver.Chrome()` instance was initialized to launch a browser.
  - The specific URL `https://pmc.ncbi.nlm.nih.gov/articles/PMC8548039/table/germs-11-03-391-t002/?report=objectonly` was accessed, targeting a table (`germs-11-03-391-t002`).
  - The page source was retrieved, parsed with `BeautifulSoup`, and the table was extracted.
  - Table rows were iterated, and column data was collected into a list, which was then converted into a `pandas` DataFrame (`df`).
  - The browser was closed with `driver.quit()`.
  - The first five rows of the DataFrame were printed with `df.head()`.
- **Outcome:** The DataFrame contained columns: `State`, `No. of cases`, `% of cases`, `No. of deaths`, `% of deaths`, `CFR` (Case Fatality Rate), and `No. of tests`, with data for 37 Nigerian states. Example data included Lagos with 57,581 cases and 439 deaths.
- **Purpose:** This step successfully scraped the COVID-19 data table, providing a dataset to merge with the CVI data for further analysis.

### 6. Data Cleaning and Preparation
- **Implicit Action:** The scraped data includes comma-separated numbers (e.g., "57,581") and percentages, which are stored as strings. No explicit cleaning (e.g., converting to numeric types) was performed in the provided code, but this would be necessary for quantitative analysis.
- **Purpose:** The raw data was structured into a usable format, though additional preprocessing (e.g., removing commas, converting types) would enhance compatibility with the CVI dataset.

### 7. Correlation Analysis and Visualization
- **Action:**
  - A heatmap was created using `seaborn.heatmap` to visualize correlations between `No. of cases`, `No. of deaths`, `No. of tests`, and `CFR`.
  - The figure size was set to `(8, 6)`, and annotations were added to display correlation values with a `coolwarm` color map.
  - The plot was titled "Correlation Between Key COVID-19 Metrics" and displayed.
- **Outcome:** The heatmap likely revealed relationships, such as a strong positive correlation between `No. of cases` and `No. of deaths`, or a weaker correlation with `CFR`, depending on the data.
- **Purpose:** This visualization helped identify how these metrics interrelate, providing insights into the pandemic's impact across Nigerian states.

### 8. Integration with CVI Data
- **Context:** Although not explicitly coded in `ncdc.ipynb`, the project’s intent (based on prior context) is to merge this pandemic data with the `cvi_nigeria` DataFrame from the earlier analysis. This would involve:
  - Matching `State` columns from both datasets.
  - Converting string numbers (e.g., "57,581") to integers/float using `pd.to_numeric(df['No. of cases'].str.replace(',', ''))`.
  - Computing correlations or joint visualizations (e.g., scatter plots of `CVI_Nigeria` vs. `No. of cases`).
- **Purpose:** Integrating these datasets would allow for a comprehensive analysis of how vulnerability indices correlate with COVID-19 outcomes.

## Summary of Achievements
- **Data Acquisition:** Successfully extracted COVID-19 data (cases, deaths, tests, CFR) for 37 Nigerian states using Selenium after an initial failed attempt with `requests`.
- **Data Structuring:** Organized the data into a `pandas` DataFrame for easy manipulation.
- **Visualization:** Created a correlation heatmap to explore relationships between key pandemic metrics.
- **Foundation for Further Analysis:** Provided a dataset that can be merged with the CVI data for deeper insights into vulnerability and pandemic impact.

## Potential Improvements
- **Data Cleaning:** Convert string data (e.g., "57,581") to numeric values and handle missing or inconsistent state names.
- **Error Handling:** Add try-except blocks for web scraping to manage potential failures.
- **Expanded Visualizations:** Include plots like scatter plots or bar charts combining CVI and pandemic data.
- **Statistical Analysis:** Perform regression or hypothesis testing to quantify relationships.

## Next Steps
This project lays a solid groundwork for understanding COVID-19's distribution and impact in Nigeria, with room to expand into a more detailed epidemiological study by integrating the CVI dataset. Let me know if you'd like to proceed with merging the datasets or creating additional visualizations!

## Current Date and Time
- Today's date and time is 05:01 PM WAT on Tuesday, June 24, 2025.
