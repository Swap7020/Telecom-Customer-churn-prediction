# 📊 Customer Churn Prediction App

## 🚀 Overview

This project is a **Machine Learning Web Application** that predicts whether a customer is likely to **churn (leave the service)** or not.

The app is built using **Streamlit** and uses a **Scikit-learn Pipeline** for robust preprocessing and prediction, ensuring no feature mismatch errors.

---

## 🎯 Features

* 🔮 Predict customer churn using manual input
* 📂 Batch prediction using CSV upload
* 🔢 Displays churn probability
* ⚡ Real-time prediction with interactive UI
* 🧠 Uses ML Pipeline (OneHotEncoder + Logistic Regression)
* ✅ Handles unseen categories automatically

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Machine Learning**: Scikit-learn
* **Libraries**: Pandas, NumPy

---

## 📁 Project Structure

```bash
Customer-Churn-Prediction/
│
├── app.py                     # Streamlit application
├── model.pkl                  # Trained ML pipeline model
├── Telco_Customer_Churn.csv   # Dataset
├── notebook.ipynb             # Model training notebook
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
└── .gitignore
```

---

## 🧠 Model Details

* **Algorithm**: Logistic Regression
* **Preprocessing**:

  * OneHotEncoder (categorical features)
  * `handle_unknown='ignore'` for unseen categories
* **Pipeline**:

  * ColumnTransformer + Logistic Regression

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Usage

### 🔹 Manual Prediction

* Enter customer details
* Click **Predict**
* View churn result and probability

### 🔹 Batch Prediction

* Upload a CSV file
* Get predictions for multiple customers
* Download results

---

## 📊 Dataset

* **Telco Customer Churn Dataset**
* Contains:

  * Customer demographics
  * Services subscribed
  * Billing information

---

## 🧪 Example Output

* ✅ Customer will stay
* ❌ Customer will churn
* 🔢 Probability score

---

## 🌐 Live Demo

👉 Add your deployed link here

```
https://your-app-name.streamlit.app
```

---

## 🔮 Future Improvements

* 📊 Add visualization dashboard
* 🔐 User authentication
* 🌐 Cloud deployment enhancements
* 🧠 Explainable AI (SHAP)

---

## 👨‍💻 Author

**Swapnil**
Final Year Engineering Student

---

## ⭐ Key Highlights

* ✅ End-to-end ML project
* ✅ Deployment-ready
* ✅ Industry-standard pipeline
* ✅ Clean and interactive UI

---

## 📌 Note

This project demonstrates a **complete machine learning lifecycle**:

* Data preprocessing
* Model training
* Model deployment

---
web application URL-- https://telecom-customer-churn-prediction-ycwjs5vchgdjdhs4sy6k7g.streamlit.app/
