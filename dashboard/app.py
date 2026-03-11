import streamlit as st
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/jobs_clean.csv")

st.title("UK Data Jobs Intelligence Dashboard")

st.write("### Dataset Preview")
st.dataframe(df.head())

# Salary statistics
st.write("### Average Salary")

avg_min = df["salary_min"].mean()
avg_max = df["salary_max"].mean()

st.write(f"Average Minimum Salary: £{avg_min:,.0f}")
st.write(f"Average Maximum Salary: £{avg_max:,.0f}")

# Top companies hiring
st.write("### Top Hiring Companies")

top_companies = df["company"].value_counts().head(10)

st.bar_chart(top_companies)

# Top locations
st.write("### Top Job Locations")

top_locations = df["location"].value_counts().head(10)

st.bar_chart(top_locations)