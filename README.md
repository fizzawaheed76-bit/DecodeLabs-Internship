# Project 2 - Data Classification Using AI

## Project Overview

This project is part of the DecodeLabs internship. It demonstrates a
basic supervised machine learning classification model using student
data.

The model predicts a student's `Result` (Pass or Fail) using:

-   Study Hours
-   Attendance
-   Previous Marks

A **Decision Tree Classifier** is used for classification.

## Project Goals

-   Load and understand a dataset
-   Select features and a target
-   Split data into training and testing sets
-   Apply a classification algorithm
-   Train the model
-   Make predictions
-   Evaluate the model

## Technologies Used

-   Python
-   Pandas
-   Scikit-learn
-   Decision Tree Classifier

## Dataset

The dataset is expected to contain these columns:

  Column            Description
  ----------------- ----------------------------
  `StudyHours`      Number of hours studied
  `Attendance`      Student attendance
  `PreviousMarks`   Student's previous marks
  `Result`          Target class: Pass or Fail

## Machine Learning Workflow

``` text
Dataset
   ↓
Load Data
   ↓
Understand Data
   ↓
Select Features and Target
   ↓
Train-Test Split
   ↓
Decision Tree Classifier
   ↓
Train Model
   ↓
Make Predictions
   ↓
Evaluate Model
```

## Features and Target

The input features are:

``` python
X = df[["StudyHours", "Attendance", "PreviousMarks"]]
```

The target is:

``` python
y = df["Result"]
```

## Train-Test Split

The project uses an 80/20 split:

-   80% for training
-   20% for testing

``` python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

## Classification Algorithm

The project uses:

``` python
model = DecisionTreeClassifier(random_state=42)
```

The model is trained with:

``` python
model.fit(X_train, y_train)
```

## Model Evaluation

The project evaluates the model using:

``` python
accuracy_score(y_test, y_pred)
```

and:

``` python
classification_report(y_test, y_pred)
```

## New Student Prediction

The code also predicts a new student's result:

``` python
new_student = [[7, 85, 68]]
prediction = model.predict(new_student)
```

The values represent:

-   Study Hours = 7
-   Attendance = 85
-   Previous Marks = 68

## Installation

Install the required libraries:

``` bash
pip install pandas scikit-learn
```

## How to Run

The current project code loads the CSV from this Google Colab path:

``` python
df = pd.read_csv("/content/drive/MyDrive/student.csv.csv")
```

If you are running the project in VS Code, place the CSV file in the
project folder and use:

``` python
df = pd.read_csv("student.csv.csv")
```

Then run:

``` bash
python decode_lab_project_2.py
```

## Skills Learned

-   Data handling with Pandas
-   Feature and target selection
-   Train-test splitting
-   Supervised learning basics
-   Classification
-   Decision Tree
-   Model training
-   Prediction
-   Accuracy evaluation
-   Classification report

## Project Information

**Internship:** DecodeLabs\
**Project:** Project 2 - Data Classification Using AI
