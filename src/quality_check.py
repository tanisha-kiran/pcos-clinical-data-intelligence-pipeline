import os
import json
import logging
from datetime import datetime
import pandas as pd


def setup_logger():
    os.makedirs("data/logs", exist_ok=True)
    logger = logging.getLogger("qa_logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("data/logs/qa.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(fh)
    return logger


def run_quality_checks(file_path):
    logger = setup_logger()
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return None

    df = pd.read_csv(file_path)

    missing = df.isnull().sum().to_dict()
    duplicates = int(df.duplicated().sum())

    invalid_bmi = 0
    if "BMI" in df.columns:
        try:
            invalid_bmi = int(df[df["BMI"] <= 0].shape[0])
        except Exception:
            invalid_bmi = 0

    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "total_records": len(df),
        "duplicate_records": duplicates,
        "invalid_bmi_values": invalid_bmi,
        "missing_values": missing,
    }

    os.makedirs("data/logs", exist_ok=True)
    with open("data/logs/qa_report.json", "w") as f:
        json.dump(report, f, indent=2)

    logger.info("QA report generated")
    logger.info(json.dumps(report))
    return report


if __name__ == "__main__":
    run_quality_checks("data/processed/pcos_enriched.csv")