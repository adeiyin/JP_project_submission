Below is a detailed summary of the Jupyter Notebook project (`state budget.ipynb`) converted into a README file format. This README explains all steps performed in the notebook, including library imports, data loading, filtering, column renaming, data exploration, and visualization, based on the provided content.

---
# Nigerian State Budget Analysis – Impact of COVID-19

This project analyzes the effect of the COVID-19 pandemic on Nigerian state budgets. It leverages a dataset comparing **original vs. revised budgets** for various states, allowing us to understand the **economic contraction** due to the pandemic.

---

## Dataset Description

The dataset includes:
- `State`: Nigerian states.
- `Original Budget`: The budget initially planned before COVID-19.
- `Revised Budget`: The revised/adjusted budget due to COVID-19 impact.

---

## Step-by-Step Analysis

### 1. **Data Import & Cleaning**
- The CSV file is loaded using Pandas.
- Column names are cleaned and renamed for readability:
  - `State` → Name of the Nigerian state.
  - `Original Budget` → Original budget before COVID-19.
  - `Revised Budget` → Revised budget after COVID-19.
  - A new column `Budget Difference` is computed as:  
    `Budget Difference = Original - Revised`

### 2. **Data Overview**
- Summary statistics are displayed using `describe()`.
- A preview of the data using `head()`.

---

## Visualizations

### 3.1 Bar Chart - Budget Comparison
- A **grouped bar chart** shows each state's **Original vs. Revised** budget.
- This visually highlights states with the biggest reductions.

### 3.2 Bar Chart - Budget Loss by State
- A **horizontal bar chart** of the `Budget Difference`.
- States are sorted by largest to smallest budget reduction.

### 3.3 Pie Chart - Top States with Highest Budget Loss
- A pie chart shows the **top 5 states** that contributed most to the national budget loss.

### 3.4 Correlation Heatmap
- A heatmap of correlations among numerical columns (`Original`, `Revised`, `Difference`) reveals the strength of their relationships.

---

## Key Insights

- All states saw a **reduction in budget** post-COVID-19.
- States like **Lagos** and **Rivers** had the largest reductions.
- There's a **strong positive correlation** between original and revised budgets, showing proportional cuts.
- The **magnitude of budget cuts** varied widely across states.

---

## Technologies Used

- **Python**
- **Pandas**
- **Matplotlib & Seaborn**
- **Jupyter Notebook**

---

## How to Run

1. Clone this repo or download the `.ipynb` file.
2. Open in Jupyter Notebook or Google Colab.
3. Ensure you have required libraries: `pandas`, `matplotlib`, `seaborn`.
--- 

This README encapsulates all steps in the notebook, provides setup instructions, and highlights areas for improvement. 


