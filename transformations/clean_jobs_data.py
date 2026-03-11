import pandas as pd
import os

# Load raw dataset
df = pd.read_csv("data/raw/jobs_raw.csv")

# Select useful columns
df = df[
    [
        "title",
        "company.display_name",
        "location.display_name",
        "salary_min",
        "salary_max",
        "category.label",
        "created",
    ]
]

# Rename columns
df = df.rename(
    columns={
        "company.display_name": "company",
        "location.display_name": "location",
        "category.label": "category",
    }
)

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Save cleaned dataset
df.to_csv("data/processed/jobs_clean.csv", index=False)

print("Clean dataset created successfully")