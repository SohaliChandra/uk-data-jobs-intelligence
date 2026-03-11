import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

url = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={APP_ID}&app_key={APP_KEY}&what=data%20engineer&where=London&results_per_page=50"

response = requests.get(url)

data = response.json()

jobs = data["results"]

df = pd.json_normalize(jobs)

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/jobs_raw.csv", index=False)

print("Jobs data saved successfully.")