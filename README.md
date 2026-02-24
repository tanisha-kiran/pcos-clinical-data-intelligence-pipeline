# PCOS Clinical Data Intelligence Pipeline

This repository contains a small data pipeline for processing and modeling PCOS clinical data.

## Contents
- `src/` — pipeline scripts (download, preprocessing, enrichment, quality checks, modeling)
- `data/` — raw and processed data (not committed)
- `notebook/` — demo notebook
- `run_pipeline.py` — convenience wrapper that runs the pipeline and saves a timestamped log

## Visualizations
Feature visualizations generated during exploration:

### BMI Category Distribution
<img width="543" height="510" alt="image" src="https://github.com/user-attachments/assets/510cf39b-d8ee-44d3-9821-c3ec66c1cb41" />


### Correlation with PCOS label
<img width="664" height="413" alt="image" src="https://github.com/user-attachments/assets/7145e24c-7dd9-4de5-bea2-6efa1c2930f3" />


## Quickstart
1. Create a virtual environment and install dependencies:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the pipeline (uses the project's `venv` when available):

```powershell
venv\Scripts\python.exe run_pipeline.py
```

3. QA and model reports will be saved to `data/logs/`.

## Notes
- Data files and logs are excluded from version control via `.gitignore`.
- To include additional plots in the README, add the image files to the repository root and update this file.

---
Generated README including visual artifacts.

