# 💳 Enterprise Credit Card Fraud Detection & Risk Analysis

> Power BI dashboard analysing 100,000+ transactions to surface $544,910 in fraudulent activity. Built during internship at Amdox Technologies.

## 📌 Project Overview

An enterprise-grade fraud detection and risk analysis system developed for a financial dataset of 100,000+ credit card transactions. The dashboard provides real-time KPIs, geospatial fraud intelligence, and AI-driven root cause analysis — replacing a legacy spreadsheet workflow.

---

## 📊 Key Results

| Metric | Value |
|---|---|
| Total Transactions Analysed | **100,000+** |
| Fraudulent Value Detected | **$544,910** |
| Fraud Rate | **1.00%** |
| Average Fraud Transaction Value | **$537** |
| Reporting Latency Reduction | **60%** vs legacy spreadsheets |
| False Positive Rate Improvement | **15%** |

---

## 🎯 Dashboard Features

### 1. Real-Time KPI Layer
DAX measures computing fraud percentage, average fraud value, and transaction velocity — updated dynamically on every filter interaction.

### 2. AI Decomposition Trees & Key Influencers
Used Power BI's built-in AI visuals to statistically correlate fraud probability with:
- Transaction type (online vs in-store vs ATM)
- Merchant category
- Time of day / day of week patterns

### 3. Geospatial Heatmaps
Location-based fraud hotspot analysis pinpointing high-risk regions (New York, Chicago). Enables regional risk teams to prioritise investigation resources.

### 4. Risk Profile Analysis Module
Segments fraud into two anomaly classes:
- **Purchasing anomalies** — unusually high-value or high-frequency purchases
- **Refund anomalies** — suspicious refund patterns indicating return fraud

This segmentation reduced false positive flagging by 15%.

### 5. High-Risk Value Filter
Advanced DAX filtering logic isolates transactions >$800 for priority review.

---

## 🛠 Tech Stack

- **Visualisation:** Power BI Desktop
- **DAX:** Custom measures for KPIs, time intelligence, risk segmentation
- **Power Query:** Data cleaning, null imputation (8% missing geolocation fields resolved via merchant zip-code lookup)
- **Python (Pandas/NumPy):** Pre-processing pipeline and synthetic data generation

---

## 🗂 Repository Contents

```
Credit-Card-Fraud-Detection/
├── Credit_fraud.pbix           # Power BI dashboard file
├── Credit_fraud.pdf            # Static dashboard export (preview)
├── main.py                     # Python data pre-processing pipeline
├── credit_card_fraud_dataset.csv
└── README.md
```

---

## 🚀 How to Open

1. Download `Credit_fraud.pbix`
2. Open with [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free)
3. All data is embedded — no external connections needed

---

## 📸 Dashboard Preview

*(See PDF export in repo for full dashboard screenshots)*

---

*Built at Amdox Technologies · Part of [Alok Verma's](https://alokvermaconnect-make.github.io/alok-verma-portfolio/) project portfolio.*# 💳 Enterprise Credit Card Fraud Detection & Risk Analysis

> Power BI dashboard analysing 100,000+ transactions to surface $544,910 in fraudulent activity. Built during internship at Amdox Technologies.

[![Power BI](https://img.shields.io/badge/Power_BI-Advanced-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com)
[![Python](https://img.shields.io/badge/Python-Data_Pipeline-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

---

## 📌 Project Overview

An enterprise-grade fraud detection and risk analysis system developed for a financial dataset of 100,000+ credit card transactions. The dashboard provides real-time KPIs, geospatial fraud intelligence, and AI-driven root cause analysis — replacing a legacy spreadsheet workflow.

---

## 📊 Key Results

| Metric | Value |
|---|---|
| Total Transactions Analysed | **100,000+** |
| Fraudulent Value Detected | **$544,910** |
| Fraud Rate | **1.00%** |
| Average Fraud Transaction Value | **$537** |
| Reporting Latency Reduction | **60%** vs legacy spreadsheets |
| False Positive Rate Improvement | **15%** |

---

## 🎯 Dashboard Features

### 1. Real-Time KPI Layer
DAX measures computing fraud percentage, average fraud value, and transaction velocity — updated dynamically on every filter interaction.

### 2. AI Decomposition Trees & Key Influencers
Used Power BI's built-in AI visuals to statistically correlate fraud probability with:
- Transaction type (online vs in-store vs ATM)
- Merchant category
- Time of day / day of week patterns

### 3. Geospatial Heatmaps
Location-based fraud hotspot analysis pinpointing high-risk regions (New York, Chicago). Enables regional risk teams to prioritise investigation resources.

### 4. Risk Profile Analysis Module
Segments fraud into two anomaly classes:
- **Purchasing anomalies** — unusually high-value or high-frequency purchases
- **Refund anomalies** — suspicious refund patterns indicating return fraud

This segmentation reduced false positive flagging by 15%.

### 5. High-Risk Value Filter
Advanced DAX filtering logic isolates transactions >$800 for priority review.

---

## 🛠 Tech Stack

- **Visualisation:** Power BI Desktop
- **DAX:** Custom measures for KPIs, time intelligence, risk segmentation
- **Power Query:** Data cleaning, null imputation (8% missing geolocation fields resolved via merchant zip-code lookup)
- **Python (Pandas/NumPy):** Pre-processing pipeline and synthetic data generation

---

## 🗂 Repository Contents

```
Credit-Card-Fraud-Detection/
├── Credit_fraud.pbix           # Power BI dashboard file
├── Credit_fraud.pdf            # Static dashboard export (preview)
├── main.py                     # Python data pre-processing pipeline
├── credit_card_fraud_dataset.csv
└── README.md
```

---

## 🚀 How to Open

1. Download `Credit_fraud.pbix`
2. Open with [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free)
3. All data is embedded — no external connections needed

---

## 📸 Dashboard Preview

*(See PDF export in repo for full dashboard screenshots)*

---

*Built at Amdox Technologies · Part of [Alok Verma's](https://alokvermaconnect-make.github.io/alok-verma-portfolio/) project portfolio.*

## 📸 Dashboard Preview
<img width="1401" height="788" alt="image" src="https://github.com/user-attachments/assets/3f5e6786-7f2c-45b3-85b1-8a9d5e3a7a28" />
<img width="1365" height="763" alt="image" src="https://github.com/user-attachments/assets/dbf5817c-f738-4d82-b173-4f04962a6bac" />
<img width="1408" height="837" alt="image" src="https://github.com/user-attachments/assets/ec8feb5c-5461-4c4f-b5ae-69230240e5ef" />
<img width="1024" height="615" alt="image" src="https://github.com/user-attachments/assets/0954328b-b6c5-42a4-ae95-4b93a7f74e18" />
<img width="1415" height="837" alt="image" src="https://github.com/user-attachments/assets/866f4b23-77b3-408c-a603-82197360d92c" />
<img width="1415" height="832" alt="image" src="https://github.com/user-attachments/assets/654794ed-c7bb-477b-b854-dd382fd1c3e6" />
<img width="1416" height="837" alt="image" src="https://github.com/user-attachments/assets/eee29ee9-1025-4cbc-9472-516ee22780cc" />
<img width="1402" height="782" alt="image" src="https://github.com/user-attachments/assets/5cc1e22b-d671-4478-afa4-1324aff8c2bd" />
