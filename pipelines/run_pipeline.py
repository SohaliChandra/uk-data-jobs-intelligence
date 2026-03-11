import subprocess
import sys
from datetime import datetime
from pathlib import Path

python_executable = sys.executable

log_folder = Path("docs/logs")
log_folder.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
log_file = log_folder / f"pipeline_log_{timestamp}.txt"


def write_log(message):
    print(message)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")


write_log("=== PIPELINE STARTED ===")
write_log(f"Start time: {datetime.now()}")

# Step 1: ingestion
write_log("Running ingestion script...")
ingestion_result = subprocess.run([python_executable, "ingestion/fetch_jobs_api.py"])

if ingestion_result.returncode != 0:
    write_log("Ingestion failed.")
    write_log("=== PIPELINE FAILED ===")
    sys.exit(1)

write_log("Ingestion completed successfully.")

# Step 2: transformation
write_log("Running transformation script...")
transformation_result = subprocess.run([python_executable, "transformations/clean_jobs_data.py"])

if transformation_result.returncode != 0:
    write_log("Transformation failed.")
    write_log("=== PIPELINE FAILED ===")
    sys.exit(1)

write_log("Transformation completed successfully.")
write_log(f"End time: {datetime.now()}")
write_log("=== PIPELINE COMPLETED SUCCESSFULLY ===")