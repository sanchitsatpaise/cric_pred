# 🏏 IPL Win Probability Predictor (Logistic Regression)

This project is an **IPL Win Probability Prediction System** that estimates the real-time chances of winning for both teams during an IPL match. The model is built using **Logistic Regression** and implemented through a **Scikit-learn Pipeline**, ensuring clean preprocessing, scalability, and reliable predictions. The application dynamically updates win probabilities based on live match conditions.

**APP LINK:https://cricpredapp.streamlit.app/**
---

## 📌 1. Project Objective

The primary objectives of this project are:

* Predict the winning probability of both teams during an IPL match
* Use real-time match parameters such as score and overs
* Build an end-to-end ML pipeline with proper preprocessing
* Deploy a clean, interactive prediction system (e.g., Streamlit)

---

## 📌 2. Problem Statement

In limited-overs cricket, match outcomes change rapidly based on:

* Runs scored
* Overs completed
* Wickets fallen
* Required run rate

This project models these factors mathematically and statistically to provide **dynamic win probabilities**, helping users understand match momentum in real time.

---

## 📌 3. Dataset Description

The dataset consists of historical IPL match and ball-by-ball data containing:

* **Batting Team**
* **Bowling Team**
* **Venue (City)**
* **Target Score**
* **Current Score**
* **Overs Completed**
* **Wickets Fallen**

This data is used to learn patterns that influence match outcomes.

---

## 📌 4. Feature Engineering (Step-by-Step)

### 🔹 Step 1: Match State Features

From raw match data, the following real-time features are calculated:

* **Runs Left** = Target − Current Score
* **Balls Left** = 120 − Balls Bowled
* **Wickets Remaining** = 10 − Wickets Fallen

---

### 🔹 Step 2: Run Rate Calculations

* **Current Run Rate (CRR)** = Current Score / Overs Completed
* **Required Run Rate (RRR)** = Runs Left / (Balls Left / 6)

These features capture match pressure and scoring momentum.

---

## 📌 5. Data Preprocessing Pipeline

A **Scikit-learn Pipeline** is used to ensure consistent and automated preprocessing:

### 🔹 Categorical Features

* Batting Team
* Bowling Team
* Venue (City)

➡ Processed using **OneHotEncoder** to convert categorical values into numerical format.

### 🔹 Numerical Features

* Runs Left
* Balls Left
* Wickets Remaining
* CRR
* RRR

➡ Passed directly to the model without scaling (Logistic Regression handles this efficiently).

---

## 📌 6. Model Selection

### 🔹 Logistic Regression

* Chosen for its **probabilistic output**
* Interpretable and efficient
* Well-suited for binary classification (Win / Loss)

The model predicts the probability of the batting team winning the match.

---

## 📌 7. Model Training

* Split data into training and testing sets
* Trained Logistic Regression within the pipeline
* Evaluated using accuracy and probability consistency

The pipeline ensures there is **no data leakage** during training and inference.

---

## 📌 8. Prediction Logic

### 🔹 How prediction works:

1. User inputs current match state
2. Pipeline preprocesses categorical and numerical features
3. Logistic Regression outputs win probability
4. Probabilities are converted into percentages for both teams

Example:

* Team A Win Probability: **68%**
* Team B Win Probability: **32%**

---

## 📌 9. Real-Time Prediction Capability

* The model recalculates probabilities after every over or ball
* Reflects changes in wickets, runs, and required rate instantly
* Provides realistic match progression insights

---

## 📌 10. Deployment

The model can be deployed using **Streamlit**, offering:

* Team and venue selection
* Input for current score, overs, wickets
* Real-time win probability visualization
* Clean and responsive UI

---

## 📌 11. Project Workflow Summary

1. Load historical IPL data
2. Engineer match-state features
3. Build preprocessing pipeline
4. Train Logistic Regression model
5. Generate win probabilities
6. Deploy as a web application

---

## 📌 12. Key Features

✅ Real-time win probability prediction
✅ End-to-end Scikit-learn pipeline
✅ Interpretable Logistic Regression model
✅ Dynamic match state analysis
✅ No external API dependency

---

## 📌 13. Technologies Used

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle / Joblib**

---

## 📌 14. Future Enhancements

* Use advanced models (XGBoost, Random Forest)
* Include ball-by-ball prediction
* Add match visualization graphs
* Extend to T20 leagues beyond IPL

---

## 📌 15. Conclusion

This IPL Win Probability Predictor showcases how **machine learning pipelines and statistical modeling** can be used to analyze real-time sports data. The project demonstrates strong concepts in feature engineering, preprocessing, and deployment, making it both production-ready and interview-friendly.

---

⭐ *If you found this project useful, consider giving it a star on GitHub!*
