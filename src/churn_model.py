import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

data = pd.read_csv("../data/customer-churn-training.csv")

print("Dataset:")
print(data)

# --------------------------------------------------
# 2. Basic information
# --------------------------------------------------

print("\nDataset shape:")
print(data.shape)

print("\nColumn information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())

print("\nChurn distribution:")
print(data["churned"].value_counts())

# --------------------------------------------------
# 3. Visualize churn distribution
# --------------------------------------------------

plt.figure(figsize=(6, 4))

sns.countplot(x="churned", data=data)

plt.title("Customer Churn Distribution")
plt.xlabel("Churned (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("../outputs/churn_distribution.png")
plt.show()

# --------------------------------------------------
# 4. Separate features and target
# --------------------------------------------------

X = data.drop(columns=["churned", "customer_id"])

y = data["churned"]

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:")
print("churned")

# --------------------------------------------------
# 5. Define numerical and categorical columns
# --------------------------------------------------

numeric_features = [
    "tenure_months",
    "support_tickets",
    "monthly_spend_inr",
    "last_login_days"
]

categorical_features = [
    "plan_type"
]

# --------------------------------------------------
# 6. Preprocessing
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# --------------------------------------------------
# 7. Machine Learning model
# --------------------------------------------------

model = LogisticRegression(
    max_iter=1000
)

pipeline = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("model", model)
    ]
)

# --------------------------------------------------
# 8. Train-test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# --------------------------------------------------
# 9. Train model
# --------------------------------------------------

pipeline.fit(X_train, y_train)

print("\nModel training completed.")

# --------------------------------------------------
# 10. Prediction
# --------------------------------------------------

y_pred = pipeline.predict(X_test)

# --------------------------------------------------
# 11. Evaluation
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

print("\nModel Evaluation")
print("----------------")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)

# --------------------------------------------------
# 12. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.tight_layout()
plt.savefig("../outputs/confusion_matrix.png")
plt.show()

print("\nProject completed successfully!")