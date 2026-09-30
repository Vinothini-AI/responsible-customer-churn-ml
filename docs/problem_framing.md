# ML Problem-Framing Memo

## Project Title

Responsible Customer Churn Prediction Using Machine Learning

## 1. Decision

The business decision is whether a customer should be considered for
voluntary retention outreach.

The model should support human decision-making rather than automatically
cancel, restrict, or penalize a customer's account.

## 2. Prediction Target

The prediction target is `churned`.

0 = customer did not churn

1 = customer churned

## 3. Unit of Observation

One row represents one customer.

## 4. Action Window

The prediction would ideally be made before a customer is expected to churn,
so that the company can offer appropriate voluntary retention support.

## 5. Non-ML Baseline

A simple non-ML baseline is to use a predefined business rule or the
majority class.

The majority class in this dataset is non-churned customers.

## 6. Why ML?

Machine learning may help identify patterns across multiple customer
attributes such as tenure, support tickets, spending, login activity,
and plan type.

However, the current dataset is very small and should only be treated
as a demonstration dataset.

## 7. False Positive

A false positive occurs when the model predicts churn but the customer
would not actually churn.

Possible consequence:
unnecessary retention communication or incentives.

## 8. False Negative

A false negative occurs when the model predicts that a customer will not
churn but the customer actually churns.

Possible consequence:
a potentially useful retention opportunity may be missed.

## 9. Human Review

Predictions should be reviewed by an appropriate business team before
important customer actions are taken.

## 10. Rollback

If monitoring shows unacceptable model errors, unexpected behavior,
or data quality problems, the ML system should be disabled and the
non-ML baseline should be used.