# Phishing URL Detection System

## Project Overview

The Phishing URL Detection System is a machine learning-based web application that detects whether a URL is **phishing** or **legitimate**.
It analyzes different URL features and predicts the result using a trained ML model.

## Problem Statement

Phishing attacks are one of the most common cyber threats today. Attackers create fake websites to steal sensitive information such as passwords, credit card details, and personal data. This project aims to detect phishing URLs automatically using machine learning techniques.

## Solution

This system extracts important features from a URL and feeds them into a trained machine learning model to predict whether the URL is safe or malicious.

## Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* HTML

## Project Structure

Phishing_detection/

app.py → Flask web application
train_model.py → ML model training
feature_extractor.py → Extracts URL features
model.pkl → Trained machine learning model
feature_columns.pkl → Feature column list
dataset.csv → Training dataset
templates/ → HTML files for UI

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/hitha28/Phishing-URL-Detection.git
```

2. Navigate to the project folder

```
cd Phishing-URL-Detection
```

3. Install required libraries

```
pip install flask pandas scikit-learn
```

4. Run the application

```
python app.py
```

5. Open the browser and go to

```
http://127.0.0.1:5000
```

## Output

The user enters a URL and the system predicts whether it is:

* Phishing Website
* Legitimate Website

## Future Improvements

* Add more advanced machine learning models
* Improve UI design
* Deploy the application online

## Author

Sreehitha M
