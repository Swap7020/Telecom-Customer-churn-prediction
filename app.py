import streamlit as st
import pickle
import pandas as pd

# Load trained pipeline model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction App")
st.write("Predict whether a customer will churn or not")

# -----------------------------
# MANUAL INPUT
# -----------------------------
st.subheader("🧾 Enter Customer Details")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72)

phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# 🔥 MISSING FEATURES ADDED
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

# Create input dataframe (ALL columns must match training)
input_df = pd.DataFrame([{
    'gender': gender,
    'SeniorCitizen': senior,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'PhoneService': phone,
    'MultipleLines': multiple,
    'InternetService': internet,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'Contract': contract,
    'PaperlessBilling': paperless,
    'PaymentMethod': payment,
    'MonthlyCharges': monthly,
    'TotalCharges': total
}])

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🔮 Predict"):
    prediction = model.predict(input_df)[0]

    try:
        prob = model.predict_proba(input_df)[0][1]
        st.write(f"🔢 Churn Probability: {prob:.2f}")
    except:
        pass

    if prediction == 1:
        st.error("❌ Customer is likely to CHURN")
    else:
        st.success("✅ Customer will STAY")

# -----------------------------
# FILE UPLOAD (BATCH)
# -----------------------------
st.subheader("📂 Batch Prediction")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.write("Preview:", df.head())

    if st.button("Predict Batch"):
        predictions = model.predict(df)

        df["Prediction"] = predictions
        df["Prediction"] = df["Prediction"].map({1: "Churn", 0: "No Churn"})

        st.write(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Results", csv, "churn_predictions.csv")