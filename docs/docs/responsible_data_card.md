# Responsible Data Card

## Dataset Purpose

This dataset is intended for demonstrating a baseline customer churn
prediction workflow.

The target is to predict whether a customer has churned.

The dataset must not be used as the sole basis for decisions such as
terminating accounts, denying services, changing prices, or penalizing
customers.

---

## Provenance and Permission

Dataset file:

customer-churn-training.csv

The available project materials do not document the original source,
data collection process, or consent/licensing conditions.

Therefore, provenance and permission should be verified before using
this dataset outside the training/demo context.

---

## Population and Representation

The dataset contains 12 customer records.

The available data does not provide sufficient information about the
larger customer population, sampling method, demographic groups, or
missing populations.

Therefore, population-level conclusions should not be made.

---

## Features and Target

### customer_id

Unique customer identifier.

This field is excluded from model training because it is an identifier
rather than a meaningful predictive feature.

### tenure_months

Number of months associated with the customer's tenure.

### support_tickets

Number of support tickets.

### monthly_spend_inr

Customer's monthly spending in INR.

### last_login_days

Number of days since the customer's last login.

### plan_type

Customer subscription plan.

Possible values include Basic, Standard, and Pro.

### churned

Target variable.

0 = did not churn

1 = churned

---

## Possible Leakage

Features should only contain information that would have been available
at the time the prediction is made.

Any information created after the churn decision or after the prediction
time could cause target leakage.

---

## Quality Checks

Number of rows: 12

Number of columns: 7

Missing values: 0

Duplicate customer IDs: 0

Churned customers: 5

Non-churned customers: 7

The small sample size is a major limitation.

---

## Risks and Safeguards

### Bias Risk

The dataset may not represent the full customer population.

Safeguard:
Collect a larger and representative dataset before production use.

### Privacy Risk

Customer-level information may be sensitive.

Safeguard:
Use appropriate access controls, minimize personally identifiable
information, and protect customer data.

### Misuse Risk

Predictions could be used to automatically penalize customers.

Safeguard:
Use predictions for voluntary retention support and human review.

### False Positive Risk

A customer may be incorrectly predicted as likely to churn.

Safeguard:
Review predictions before taking action.

### False Negative Risk

A customer who is likely to churn may be incorrectly classified as
not likely to churn.

Safeguard:
Monitor recall and conduct error analysis.

---

## Intended Evaluation

The baseline should report:

- Accuracy
- Precision
- Recall
- Confusion matrix
- Error analysis

Because the dataset is very small, evaluation results should not be
interpreted as evidence of production performance.

Future evaluation should also consider calibration, fairness,
and performance on a larger held-out dataset.