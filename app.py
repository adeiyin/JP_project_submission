import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# ===== Load model and top features =====
# ✅ Removed extra quotes
model = joblib.load("/Users/user/Documents/Jupyter_Lesson/projects/machine learning projects/Telco Churn/churn_model.pkl")
top_features = joblib.load("/Users/user/Documents/Jupyter_Lesson/projects/machine learning projects/Telco Churn/top_features.pkl")

# ===== App title and description =====
st.title("📉 Customer Churn Prediction App")
st.write("""
This app predicts whether a customer is likely to **churn** (leave the service) 
based on key features. The prediction is powered by a machine learning model.
""")

# Show top features to the user
st.subheader("Top 5 Features Used for Prediction")
st.write(", ".join(top_features))

# ===== Dynamic Input Form =====
st.subheader("Enter Customer Information")
user_input = {}
for feature in top_features:
    if "tenure" in feature.lower():
        user_input[feature] = st.slider(feature, 0, 72, 12)
    elif "charge" in feature.lower():
        user_input[feature] = st.number_input(feature, min_value=0.0, value=50.0)
    else:
        user_input[feature] = st.selectbox(feature, [0, 1])  # Binary

# ===== Predict Button =====
if st.button("Predict Churn"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # ===== Show prediction result =====
    if prediction == 1:
        st.error(f"⚠️ This customer is LIKELY to churn. (Confidence: {probability:.2%})")
    else:
        st.success(f"✅ This customer is NOT likely to churn. (Confidence: {1 - probability:.2%})")

    # ===== Interpretation help for your defense =====
    st.markdown("""
    **Interpretation:**
    - A high churn probability means the customer may be dissatisfied or at risk of leaving.
    - Businesses can use this insight to target such customers with retention offers.
    """)

