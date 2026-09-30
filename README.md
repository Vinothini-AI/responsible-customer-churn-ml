# Responsible Customer Churn Prediction

## Overview

This project demonstrates a responsible machine learning workflow for
customer churn prediction.

The project focuses not only on model training but also on problem
framing, data documentation, risk identification, evaluation, and
human oversight.

## Problem

Customer churn can create business challenges.

The objective is to predict whether a customer is likely to churn using
available customer attributes.

## Dataset

The provided dataset contains 12 customer records and the following
fields:

- customer_id
- tenure_months
- support_tickets
- monthly_spend_inr
- last_login_days
- plan_type
- churned

The dataset contains 5 churned customers and 7 non-churned customers.

There are no missing values in the provided dataset.

## Features

- Tenure in months
- Number of support tickets
- Monthly spending
- Days since last login
- Subscription plan

## Target

`churned`

0 = did not churn

1 = churned

## Model

The project uses Logistic Regression as a baseline classification model.

Categorical data is converted using OneHotEncoder.

## Evaluation

The project reports:

- Accuracy
- Precision
- Recall
- Confusion matrix
- Classification report

## Responsible ML

The project includes:

- Problem framing
- Responsible data card
- Risk register
- Human review
- False-positive analysis
- False-negative analysis
- Rollback considerations
- Data quality checks

## Important Limitation

The dataset contains only 12 records.

Therefore, the model should not be considered production-ready and
the evaluation results should not be generalized to a larger customer
population.

## Project Structure

```text
responsible-churn-ml/
│
├── data/
│   └── customer-churn-training.csv
│
├── src/
│   └── churn_model.py
│
├── outputs/
│   ├── churn_distribution.png
│   └── confusion_matrix.png
│
├── docs/
│   ├── problem_framing.md
│   ├── responsible_data_card.md
│   └── risk_register.md
│
├── README.md
├── requirements.txt
└── .gitignore