# Medical Charge Predictor

A machine learning web application that predicts medical insurance charges based on user health and demographic information such as age, BMI, smoking habits, number of children, gender, and region.

The project combines a trained Lasso Regression model with a Flask web application to provide real-time insurance cost predictions through a clean and interactive user interface.

---

# Project Overview

Medical insurance costs vary depending on multiple lifestyle and demographic factors. This project uses machine learning to estimate expected medical charges using historical insurance data.

The application allows users to:

- Enter personal and health-related details
- Predict estimated medical insurance charges instantly
- Access predictions through a simple browser-based interface
- Understand the impact of factors like smoking and BMI on insurance costs

---

# Features

- Machine Learning based insurance charge prediction
- Flask-powered web application
- Interactive HTML frontend
- Data preprocessing using feature scaling
- Trained Lasso Regression model for prediction
- Clean UI with responsive design
- Real-time prediction results

---

# Tech Stack

## Programming Language
- Python

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

## Web Framework
- Flask

## Frontend
- HTML5
- CSS3

## Model Serialization
- Pickle

---

# Project Structure

```bash
Medical-Charge-Predictor/
│
├── application.py          # Main Flask application
├── medical.ipynb           # Jupyter notebook for model training
├── insurance.csv           # Dataset used for training
├── scaler.pkl              # Saved feature scaler
├── lasso.pkl               # Trained Lasso Regression model
│
├── templates/
│   ├── index.html          # Home page
│   └── predict.html        # Prediction page
│
└── README.md
```

---

# Dataset Information

The project uses the popular Insurance Dataset containing medical and demographic information.

## Input Features

| Feature | Description |
|---|---|
| Age | Age of the individual |
| Sex | Gender of the individual |
| BMI | Body Mass Index |
| Children | Number of dependents |
| Smoker | Smoking status |
| Region | Residential region |

## Target Variable

| Variable | Description |
|---|---|
| Charges | Medical insurance cost |

---

# Machine Learning Workflow

## 1. Data Collection
The insurance dataset is loaded using Pandas.

## 2. Data Preprocessing
- Handling categorical variables
- Feature scaling using StandardScaler
- Preparing training and testing datasets

## 3. Model Training
A Lasso Regression model is trained using Scikit-learn.

## 4. Model Serialization
The trained model and scaler are saved using Pickle:

- `lasso.pkl`
- `scaler.pkl`

## 5. Web Deployment
The Flask application loads the serialized model and performs predictions on user input.

---

# Application Workflow

1. User opens the home page
2. User clicks on "Start Prediction"
3. User enters medical and demographic information
4. Flask receives the input
5. Data is scaled using the saved scaler
6. Lasso model predicts insurance charges
7. Predicted result is displayed on the webpage

---

# User Interface

## Home Page
The home page introduces the project and provides navigation to the prediction page.

## Prediction Page
Users can enter:

- Age
- Gender
- BMI
- Number of children
- Smoking status
- Region

The application then displays the predicted medical insurance charges.

---

# Installation Guide

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/medical-charge-predictor.git
cd medical-charge-predictor
```

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

---

## Step 4: Run the Application

```bash
python application.py
```

---

## Step 5: Open in Browser

Visit:

```bash
http://127.0.0.1:5000/
```

---

# Sample Input

| Parameter | Example |
|---|---|
| Age | 25 |
| Gender | Male |
| BMI | 28.5 |
| Children | 1 |
| Smoker | No |
| Region | Southeast |

---

# Sample Output

```bash
Predicted Medical Charges: ₹ 14532.67
```

---

# Important Files

## application.py
Contains:

- Flask routes
- Model loading
- Prediction logic
- Web server configuration

## medical.ipynb
Contains:

- Data analysis
- Data preprocessing
- Model training
- Model evaluation

## HTML Templates

### index.html
Landing page for the application.

### predict.html
Prediction form and result display page.

---

# Future Improvements

- Add graphical analytics dashboard
- Deploy on cloud platforms like Render or Heroku
- Add user authentication
- Improve prediction accuracy using advanced models
- Add API support
- Store prediction history in database
- Add model comparison visualizations

---

# Screenshots

Add screenshots of:

- Home Page
- Prediction Form
- Prediction Output

Example:

```markdown
![Home Page](screenshots/home.png)
![Prediction Page](screenshots/predict.png)
```

---

# Learning Outcomes

This project demonstrates:

- End-to-end machine learning workflow
- Regression model development
- Model serialization using Pickle
- Flask web development
- Frontend and backend integration
- Real-world deployment concepts

---

# Conclusion

The Medical Charge Predictor project provides a practical implementation of machine learning in the healthcare insurance domain. By integrating a trained regression model with a Flask web application, the project delivers accurate and real-time insurance charge predictions through an easy-to-use interface.

This project is suitable for:

- Machine Learning portfolios
- Academic mini projects
- Flask deployment practice
- Regression model demonstrations
- Data science learning

---

# Author

Developed as a Machine Learning and Flask integration project.

---

# License

This project is intended for educational and learning purposes.

