
import streamlit as st
import pandas as pd

# Mock client dataset
mock_client_data = pd.DataFrame({
    'client_no': [1, 2, 3],
    'client_start_date': ['2020-01-01', '2019-06-15', '2021-03-20'],
    'is_immigrant': ['N', 'Y', 'N'],
    'is_foreign_citizen': ['N', 'N', 'Y'],
    'is_local': ['Y', 'Y', 'N']
})

# Mock transaction dataset
mock_transaction_data = pd.DataFrame({
    'client_no': [1, 1, 2, 3, 3],
    'account_no': ['ACC123', 'ACC123', 'ACC456', 'ACC789', 'ACC789'],
    'product_code': ['PRD001', 'PRD002', 'PRD003', 'PRD001', 'PRD004'],
    'trade_type_desc': ['buy', 'sell', 'buy', 'subscription', 'redemption'],
    'contract_no': ['C001', 'C002', 'C003', 'C004', 'C005']
})

# Title of the app
st.title("Quick Investment Product Recommendation")

# User inputs
client_no = st.selectbox("Select Client Number", mock_client_data['client_no'])
investment_objective = st.selectbox("Investment Objective", ["Growth", "Income", "Capital Preservation", "Speculative"])
risk_tolerance = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
investment_horizon = st.selectbox("Investment Horizon", ["Short-term (0-1 year)", "Medium-term (1-5 years)", "Long-term (5+ years)"])
investment_amount = st.number_input("Amount Available for Investment", min_value=1000, step=1000)

# Fetch client data and transactions
client_transactions = mock_transaction_data[mock_transaction_data['client_no'] == client_no]

# Simulated Product Recommendation Logic
# (This is where you could include more sophisticated logic based on the inputs)
if risk_tolerance == "Low":
    recommended_product = "PRD004"  # Example: safer product
elif risk_tolerance == "High":
    recommended_product = "PRD001"  # Example: higher risk product
else:
    recommended_product = client_transactions['product_code'].mode()[0]  # Example: most frequent product

# Display Recommendation
st.header("Recommended Product")
st.write(f"Based on your preferences, we recommend: **{recommended_product}**")
