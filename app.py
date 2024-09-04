import streamlit as st
import pandas as pd
import pickle  # Import pickle for loading .pkl files
import sklearn

# Load the trained Random Forest model
with open(r'C:\Users\TARUN\MLdeploy\random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create a Streamlit app
st.title("Customer Churn Prediction App")

# Input fields for feature values on the main screen
st.header("Enter Customer Information")
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
internet_service = st.selectbox("Internet Service", ('DSL', 'Fiber optic', 'No'))
contract = st.selectbox("Contract", ('Month-to-month', 'One year', 'Two year'))
monthly_charges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=50)
total_charges = st.number_input("Total Charges", min_value=0, max_value=10000, value=0)

# Map input values to numeric using the label mapping
label_mapping = {
    'DSL': 0,
    'Fiber optic': 1,
    'No': 2,
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2,
}
internet_service = label_mapping[internet_service]
contract = label_mapping[contract]

# Make a prediction using the model
prediction = model.predict([[tenure, internet_service, contract, monthly_charges, total_charges]])

# Display the prediction result on the main screen
st.header("Prediction Result")
if prediction[0] == 0:
    st.success("This customer is likely to stay.")
else:
    st.error("This customer is likely to churn.")
