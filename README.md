# Group Project Financing Anouncement
## Big Data - Team 2

### Team Members

- **Vincenzo Vantornout** (02108145) – Vincenzo.vantornout@ugent.be  
- **Henri Bolliou** (02112399) – Henri.bolliou@ugent.be  
- **Renzo Gevaert** (02103651) – Renzo.gevaert@ugent.be  
- **Douwe Pauwels** (02105447) – Douwe.pauwels@ugent.be
- **Emile Schoemans** (02006755) – Emile.schoemans@ugent.be  


**Instructor:** Prof. Dirk Van den Poel  
**Teaching Assistant:** Dylan Van Mulders and Simon De Lange 
**Academic Year:** 2025–2026  

---

## Project Overview

This repository contains all code, documentation, and results produced by Team 2 for the Big Data course at Ghent University.

The objective of this project was to:

- Predict the impact of news articles and stock info on financing announcements using PySpark.

- Predict and analyze the relationship between multi-source information signals and financing announcements to evaluate their subsequent impact on stock price dilution and market opportunities.

- Develop strategies for a fund based on predictions regarding capital intensive mining sectors and exploration results.


## Repository Structure

```text
.
├── CEO_CA/                              # sentiment analysis on scraped CEO.CA data
│                
├── Cleaned_data/                        # parquet files created
│
├── Data/
│   ├── Categorical/                     # maturity level per ticker
│   ├── Sentiment_data/                  # parquet files of the performed sentiment analysis
│   ├── Stock_data/                      # stock data per ticker
│   └── Textual_data/                    # parquet and json files containing our scraped data, divided by source
│
├── Data_collection/                     # notebooks containing the code for scraping per source
│
├── Demo's/                              # demo's we got through Ufora
│
├── Dependent_data_collection/           # dependent data csv files + notebook to add to our basetable
│
├── Models/                              # all models used 
│   ├── Results/                         # parquet files containing the lr and gbt predictions
│
├── Sentiment_analysis/                  # notebooks and parquet files containing the sentiment analyses for our textual data
│
├── Visuals/                             # notebooks for generating our visuals
│   ├── industry_plots/                  # industry plots to gain insight
│   └── Shap_plots/                      # shap plots to gain insight in feature importance
│
└── README.md



# Data Collection & Integration: 
We combined professional financial news from De Tijd, the Financial Times, and Yahoo Finance with retail investor discussions from CEO.CA and official corporate updates from ticker websites to create a complete picture of the market.

# Feature Engineering & Sentiment Analysis: 
Using NLP models (FinBERT, VADER, and Ollama), we transformed raw textual data into predictive sentiment scores.

# Predictive Modeling: 
We utilized PySpark to handle large-scale data processing and trained machine learning models (Logistic Regression and GBT) to predict financing events in the next bi-weekly period.

# Explainability: 
We applied SHAP values to identify the primary drivers of financing announcements, providing transparency into how sentiment and market volatility influence model outcomes.
