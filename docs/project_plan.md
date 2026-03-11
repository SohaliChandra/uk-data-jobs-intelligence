PROJECT NAME
UK Data Jobs Intelligence Platform


PROJECT OBJECTIVE
Build a cloud-based data engineering pipeline that collects
UK job postings, stores raw data, processes structured datasets,
and generates analytics dashboards.


DATA SOURCE
Adzuna Job Search API


TECHNOLOGY STACK

Data Source
Adzuna API

Ingestion
Python

Raw Storage
Azure Blob Storage

Orchestration
Azure Data Factory

Data Warehouse
Azure SQL Database

Analytics
Power BI


DATA PIPELINE ARCHITECTURE

Adzuna API
    ↓
Python ingestion script
    ↓
Azure Blob Storage (Bronze Layer)
    ↓
Azure Data Factory
    ↓
Azure SQL Database (Gold Layer)
    ↓
Power BI Dashboard


EXPECTED INSIGHTS

Most in-demand job titles
Top hiring companies
Job postings by location
Salary trends
Skills demand
Job posting trends over time


PROJECT STRUCTURE

docs
ingestion
transformations
data/raw
data/processed
sql
pipelines
dashboard