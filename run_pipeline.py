# run_pipeline.py
# Runs pipeline steps using venv python and writes a timestamped log to data/logs/

import subprocess
import datetime
import os
import sys

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_dir = "data/logs"
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, f"pipeline_{timestamp}.log")

# Prefer the project's venv python, fallback to sys.executable
venv_py = os.path.join(os.path.dirname(__file__), "venv", "Scripts", "python.exe")
python_exec = venv_py if os.path.exists(venv_py) else sys.executable

commands = [
    [python_exec, "src/download_dataset.py"],
    [python_exec, "src/preprocessing.py"],
    [python_exec, "src/enrichment.py"],
    [python_exec, "src/quality_check.py"],
    [python_exec, "src/model.py"],
]

with open(log_path, "w", encoding="utf-8") as log:
    for cmd in commands:
        cmd_str = " ".join(cmd)
        header = f"\n===== Running: {cmd_str} =====\n"
        log.write(header)
        print(header, end="")

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
            print(line, end="")
            log.write(line)
        proc.wait()
        status = f"Exit code: {proc.returncode}\n"
        log.write(status)
        print(status)

        if proc.returncode != 0:
            print(f"Command failed: {cmd_str} (exit {proc.returncode}). See {log_path}")
            break

print(f"\nPipeline finished. Log saved to {log_path}")
