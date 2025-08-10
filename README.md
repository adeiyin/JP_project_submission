# Telco Customer Churn Prediction

## 1. Project Title
**Telco Customer Churn Prediction using Machine Learning & Streamlit**

---

## 2. Project Overview
This project predicts **customer churn** for a telecommunications company using historical customer data and machine learning.

**Customer churn** occurs when customers stop doing business with a company. Predicting churn is vital for telecom companies because retaining customers is more cost-effective than acquiring new ones. By identifying customers at risk, businesses can take proactive steps to retain them.

This repository includes:
- A **Jupyter Notebook** with the complete machine learning workflow.
- A **Streamlit web app** to make live predictions using the trained model.

---

## 3. Dataset Description
The dataset used is the **Telco Customer Churn dataset** from [IBM Sample Data](https://www.ibm.com/communities/analytics/watson-analytics-blog/).  

**Key details:**
- **Rows:** ~7,000 customers
- **Columns:** Customer demographics, account information, service subscriptions, and churn status.
- **Target variable:** `Churn` (Yes/No)

**Example features:**
- `gender` – Male/Female
- `SeniorCitizen` – 1 if senior citizen, else 0
- `tenure` – Number of months the customer has stayed
- `InternetService` – DSL/Fiber optic/None
- `MonthlyCharges` – The amount charged per month
- `TotalCharges` – The total amount charged
- `Contract` – Month-to-month/One year/Two year

---

## 4. Machine Learning Workflow

### **Step 1: Data Preprocessing**
- Removed missing values
- Converted categorical features using **One-Hot Encoding**
- Scaled numerical features using **StandardScaler**

### **Step 2: Dimensionality Reduction**
- Applied **PCA (Principal Component Analysis)** for visualization and potential dimensionality reduction.

### **Step 3: Feature Selection**
- Trained an initial **Random Forest Classifier** to determine **feature importance**.
- Selected the **top 5 features** contributing most to prediction accuracy.

### **Step 4: Model Training**
- Used **Random Forest Classifier** with tuned hyperparameters.
- Split data into training (80%) and test (20%) sets.
- Evaluated performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix

### **Step 5: Model Export**
- Saved the trained model as a `.pkl` file for deployment in the Streamlit app.

---

## 5. Feature Importance
The **top 5 features** selected were:
1. `tenure`
2. `MonthlyCharges`
3. `Contract_Two year`
4. `OnlineSecurity_Yes`
5. `TotalCharges`

These features matter because they directly relate to customer satisfaction, cost, and contract length — key churn indicators.

---

## 6. Application Description
The **Streamlit app** (`app.py`) provides an interactive UI where users can:
- Input customer attributes
- Get an instant **churn probability prediction**
- See whether the customer is **likely to churn** or **stay**

---

## 7. Installation Instructions

### **Requirements**
- Python 3.8+
- Required libraries:
```bash
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
```

### **Setup**
```bash
# Clone repository
git clone https://github.com/username/telco-customer-churn.git
cd telco-customer-churn

# Install dependencies
pip install -r requirements.txt
```

---

## 8. Running the Notebook
```bash
jupyter notebook "Telco Customer Churn.ipynb"
```
Run all cells sequentially to:
- Load data
- Train the model
- Save the model for deployment

---

## 9. Running the App
```bash
streamlit run app.py
```
This launches the app at **http://localhost:8501**.

---

## 10. Example Predictions
Example input:
| tenure | MonthlyCharges | Contract_Two year | OnlineSecurity_Yes | TotalCharges |
|--------|----------------|-------------------|--------------------|--------------|
| 12     | 70.35          | 0                 | 1                  | 842.50       |

**Prediction:** Customer is **Not Likely to Churn** (Probability: 0.12)

---

## 11. Folder Structure
```
telco-customer-churn/
│
├── Telco Customer Churn.ipynb   # ML pipeline
├── app.py                        # Streamlit app
├── churn_model.pkl               # Saved trained model
├── requirements.txt              # Dependencies
└── README.md                     # Project documentation
```

---

## 12. Future Improvements
- Test additional models (XGBoost, LightGBM, Neural Networks)
- Include more features (call records, payment history)
- Implement **real-time churn prediction** from live customer data
- Deploy as a cloud service (AWS/GCP/Azure)

---

## 13. Author & License
**Author:** [Your Name]  
**License:** MIT License
