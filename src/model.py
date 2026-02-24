import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def train_model(file_path, save_report=True):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    df = pd.read_csv(file_path)

    if "PCOS_(Y/N)" not in df.columns:
        print("Target column not found.")
        return None

    X = df.drop(columns=["PCOS_(Y/N)"])
    y = df["PCOS_(Y/N)"]

    # Keep only numeric columns
    X = X.select_dtypes(include=["number"]).copy()

    if X.shape[1] == 0:
        print("No numeric features available for modeling.")
        return None

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    report_text = classification_report(y_test, predictions, output_dict=False)
    report = {
        "accuracy": acc,
        "classification_report": classification_report(y_test, predictions, output_dict=True),
        "features": X.columns.tolist(),
    }

    print("Accuracy:", acc)
    print("\nClassification Report:\n")
    print(report_text)

    if save_report:
        os.makedirs("data/logs", exist_ok=True)
        with open("data/logs/model_report.json", "w") as f:
            json.dump(report, f, indent=2)

    return model


if __name__ == "__main__":
    train_model("data/processed/pcos_enriched.csv")