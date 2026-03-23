# European Fintech Job Market Analysis

## 📌 Project Overview
An end-to-end data engineering and analytics pipeline designed to extract, structure, and analyze the real-time skills demanded by the European fintech job market. 

This project bypasses traditional static datasets by utilizing custom Python web scrapers to pull live data from eFinancialCareers, analyzing over 80 active postings to determine the exact blend of technical tools (SQL, Python) and domain knowledge (Risk, Compliance) required for modern analysts.

## 🛠️ Tech Stack
* **Data Extraction:** Python, Selenium, WebDriver Manager
* **Data Processing & NLP:** Pandas
* **Data Visualization:** Tableau Public

## 📂 The Pipeline
1. **`scraper.py`:** Navigates the job board using browser automation, structurally extracts relevant job postings, and bypasses basic anti-bot security.
2. **`deep_scraper.py`:** Visits individual job URLs and utilizes Natural Language Processing (NLP) techniques to parse unstructured job descriptions, mapping qualitative text to quantitative skill matrices (1s and 0s).
3. **`efc_master_data.csv`:** The final, cleaned, and structured dataset.

## 📊 The Dashboard
The extracted data was fed into Tableau to create a dynamic, interactive dashboard analyzing the macroeconomic split between hard tech skills and financial domain expertise. 
