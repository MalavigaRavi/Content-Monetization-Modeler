# 📊 YouTube Ad Revenue Prediction using Machine Learning

A **Machine Learning project** that predicts **YouTube advertisement revenue** based on video performance metrics such as views, likes, comments, watch time, category, and audience location.

This project implements **multiple regression algorithms**, performs **feature engineering**, and deploys the model using a **Streamlit web application**.

---

# 🚀 Project Overview

YouTube creators earn revenue through advertisements. Predicting potential revenue based on engagement metrics can help creators:

* Understand video performance
* Optimize content strategy
* Estimate monetization potential

This project builds a **predictive machine learning model** to estimate **YouTube Ad Revenue (USD)**.

---

# 🎯 Problem Statement

Predict **YouTube Advertisement Revenue** using historical data containing:

* Video engagement metrics
* Audience demographics
* Video characteristics

The model predicts:

**Ad Revenue (USD)**

---

# 🧠 Machine Learning Models Used

The following regression models were implemented and compared:

1️⃣ **Linear Regression**

2️⃣ **Polynomial Regression**

3️⃣ **Decision Tree Regression**

4️⃣ **Random Forest Regression**

5️⃣ **Ridge Regression**

The best-performing model was selected and deployed in the Streamlit application.

---

# 📂 Project Structure

YouTube-Revenue-Prediction

*Data- youtube_monetization.csv

*model_training.ipynb

*Saved Model- revenue_model.pkl

*Streamlit app-app.py

# 📊 Dataset Features

The dataset contains the following attributes:

| Feature              | Description                |
| -------------------- | -------------------------- |
| views                | Total video views          |
| likes                | Number of likes            |
| comments             | Number of comments         |
| watch_time_minutes   | Total watch time           |
| video_length_minutes | Duration of video          |
| subscribers          | Channel subscriber count   |
| category             | Video category             |
| device               | Viewer device type         |
| country              | Viewer location            |
| month                | Upload month               |
| day                  | Upload day                 |
| engagement_rate      | (likes + comments) / views |

Target Variable:

**ad_revenue_usd**

---

# 🔧 Data Preprocessing

The following preprocessing steps were performed:

* Handling missing values
* Removing duplicates
* Feature engineering
* Date feature extraction
* Engagement rate calculation
* Feature scaling
* One-hot encoding for categorical variables

A **Scikit-learn Pipeline** was implemented to ensure consistent preprocessing during training and prediction.

---

# ⚙️ Feature Engineering

New features were created to improve model performance:

**Engagement Rate**

```
engagement_rate = (likes + comments) / views
```

Additional features extracted from upload date:

* Month
* Day

---

# 📈 Model Evaluation Metrics

Models were evaluated using:

* **R² Score**
* **Mean Absolute Error (MAE)**
* **Root Mean Squared Error (RMSE)**

Example evaluation:

| Model                 | R² Score |
| --------------------- | -------- |
| Linear Regression     | 0.78     |
| Polynomial Regression | 0.82     |
| Decision Tree         | 0.85     |
| Random Forest         | 0.92     |
| Ridge Regression      | 0.80     |

Random Forest performed the best and was selected for deployment.

---

# 🌐 Streamlit Web Application

A **Streamlit web application** was built for real-time predictions.

Users can input:

* Views
* Likes
* Comments
* Watch time
* Video length
* Subscribers
* Category
* Device
* Country
* Upload date

The app predicts:

**Estimated YouTube Ad Revenue**

---

# 🖥️ Application Interface

Example UI:

* User input fields
* Revenue prediction button
* Estimated revenue output

---

# 🧰 Technologies Used

Programming Language:

* Python

Libraries:

* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* streamlit
* pickle

Tools:

* Jupyter Notebook
* GitHub
* Streamlit

---

# ▶️ Run the Application

Run the Streamlit app:

bash
streamlit run app.py


# 📊 Example Prediction

Example Input:

| Feature      | Value  |
| ------------ | ------ |
| Views        | 150000 |
| Likes        | 12000  |
| Comments     | 850    |
| Watch Time   | 250000 |
| Video Length | 10     |
| Subscribers  | 50000  |

Output:

```
Estimated Ad Revenue: $1450
```

---

# 🧪 Model Training Workflow

1. Data collection
2. Data preprocessing
3. Feature engineering
4. Train-test split
5. Model training
6. Model evaluation
7. Model selection
8. Model deployment

---

# 🔐 Model Serialization

The trained model pipeline was saved using **Pickle**:

```
revenue_model.pkl
```

This ensures the same preprocessing steps are applied during prediction.

---

# 📈 Future Improvements

Possible enhancements include:

* Hyperparameter tuning
* Deep learning models
* Feature importance visualization
* Real-time YouTube API integration
* Dashboard analytics

---

# 👩‍💻 Author

**Malaviga Ravi**

Aspiring Data Scientist | Data Analyst




These make your project **look like a real production ML project**, not just a course project.
