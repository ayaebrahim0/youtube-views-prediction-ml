# youtube-views-prediction-ml
Machine Learning project to predict YouTube video views using regression models and Streamlit app.
# YouTube Video Performance Prediction using Machine Learning

## Project Overview

This project predicts YouTube video views using Machine Learning techniques based on video engagement and content-related features.

The workflow includes data preprocessing, feature engineering, model training, model comparison, evaluation, and deployment through an interactive Streamlit application.

---

## Objectives

* Predict expected YouTube video views.
* Analyze engagement metrics.
* Compare multiple Machine Learning models.
* Select the best-performing model for accurate predictions.
* Provide a user-friendly web interface using Streamlit.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib

---

## Machine Learning Workflow

### 1. Data Preprocessing

* Data Cleaning
* Handling Missing Values
* Feature Engineering
* Categorical Encoding

### 2. Model Training

Three Machine Learning models were trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
<img width="2700" height="1500" alt="models_comparison" src="https://github.com/user-attachments/assets/7c652abe-1e7a-4125-ba93-4109b3ec86f4" />
The best-performing model was selected based on evaluation metrics.

### 3. Model Evaluation

Evaluation metrics included:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

---

## Features Used

The prediction model utilizes features such as:

* Video Category
* Language
* Duration
* Likes
* Comments
* Shares
* Sentiment Score
* Engagement Metrics

---

## Streamlit Application

The project includes an interactive Streamlit application where users can:

* Enter video details
* Calculate engagement metrics
* Generate view predictions
* Assess video performance level

---

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── youtube_RandomForest_Regressor_Model.pkl
├── README.md
└── dataset.csv
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/youtube-views-prediction-ml.git
```

Move into the project directory:

```bash
cd youtube-views-prediction-ml
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Results

The Random Forest Regressor achieved the best performance among the tested models and was selected as the final prediction model.

---

## Author

Aya Ebrahim

Machine Learning Engineer | Data Analyst

```bash
pip install -r requirements.txt
streamlit run app.py
```<img width="2700" height="1500" alt="models_comparison" src="https://github.com/user-attachments/assets/7c652abe-1e7a-4125-ba93-4109b3ec86f4" />

