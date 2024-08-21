import streamlit as st
import torch
from transformers import AutoModel, AutoTokenizer
from safetensors import safe_open

# Load your safetensors model
model_path = ""\\cfi-fsvr01\User_Folders\Goldamae.Bullock\Desktop\Personal Documents\model.safetensors""
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Example: Loading a model (adjust to your specific model architecture)
tokenizer = AutoTokenizer.from_pretrained(""\\cfi-fsvr01\User_Folders\Goldamae.Bullock\Desktop\Personal Documents\model.safetensors"")
model = AutoModel.from_pretrained(""\\cfi-fsvr01\User_Folders\Goldamae.Bullock\Desktop\Personal Documents\model.safetensors"")
model.load_state_dict(torch.load("\\cfi-fsvr01\User_Folders\Goldamae.Bullock\Desktop\Personal Documents\model.safetensors"))
model.to(device)
model.eval()

# Define the app layout
st.title("Investment Product Recommendation")

# User inputs
client_no = st.selectbox("Select Client Number", [1, 2, 3])
investment_objective = st.selectbox("Investment Objective", ["Growth", "Income", "Capital Preservation", "Speculative"])
risk_tolerance = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
investment_horizon = st.selectbox("Investment Horizon", ["Short-term (0-1 year)", "Medium-term (1-5 years)", "Long-term (5+ years)"])
investment_amount = st.number_input("Amount Available for Investment", min_value=1000, step=1000)

# Preprocess inputs for the model
input_text = f"Client: {client_no}, Objective: {investment_objective}, Risk: {risk_tolerance}, Horizon: {investment_horizon}, Amount: {investment_amount}"
inputs = tokenizer(input_text, return_tensors="pt").to(device)

# Get model prediction
with torch.no_grad():
    outputs = model(**inputs)
    # Example: Postprocess model output (this depends on your specific model's output format)
    recommended_product = "ExampleProduct"  # Replace this with actual logic

# Display recommendation
st.header("Recommended Product")
st.write(f"Based on your preferences, we recommend: **{recommended_product}**")
