import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# CONFIGURATION (Matching your PDF stats)
TOTAL_RECORDS = 100000
FRAUD_RATE = 0.01  # 1%
START_DATE = datetime(2023, 10, 21)
END_DATE = datetime(2024, 10, 21)

# 1. Transaction IDs
transaction_ids = np.arange(1, TOTAL_RECORDS + 1)

# 2. Dates
date_range = (END_DATE - START_DATE).days
dates = [START_DATE + timedelta(days=random.randint(0, date_range)) for _ in range(TOTAL_RECORDS)]

# 3. Locations (Weighted to match PDF: Chicago high vol, NY high risk)
locations = ['Chicago', 'New York', 'San Diego', 'Houston', 'Dallas', 'Phoenix', 'San Jose', 'Los Angeles']
location_weights = [0.25, 0.20, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05]
loc_data = np.random.choice(locations, TOTAL_RECORDS, p=location_weights)

# 4. Transaction Types (Purchase vs Refund)
types = ['purchase', 'refund']
type_data = np.random.choice(types, TOTAL_RECORDS, p=[0.7, 0.3])

# 5. Amounts (Normal distribution around $50-$5000)
amounts = np.round(np.random.exponential(scale=500, size=TOTAL_RECORDS), 2)

# 6. Fraud Logic (Injecting the 1% Fraud)
# We make specific patterns fraudulent to match your story (e.g., Refunds in NY)
df = pd.DataFrame({
    'TransactionID': transaction_ids,
    'TransactionDate': dates,
    'Amount': amounts,
    'MerchantID': np.random.randint(1, 1000, TOTAL_RECORDS),
    'TransactionType': type_data,
    'Location': loc_data,
    'IsFraud': 0 # Default to legitimate
})

# Force exactly 1000 frauds (1%)
fraud_indices = np.random.choice(df.index, 1000, replace=False)
df.loc[fraud_indices, 'IsFraud'] = 1

# Make 'Refunds' and 'New York' slightly more fraudulent for the story
df.loc[(df['Location'] == 'New York') & (df['TransactionType'] == 'refund') & (df.index % 10 == 0), 'IsFraud'] = 1

# Limit to exactly 1000 frauds again (cleanup)
current_fraud = df[df['IsFraud'] == 1].index
if len(current_fraud) > 1000:
    drop_indices = np.random.choice(current_fraud, len(current_fraud) - 1000, replace=False)
    df.loc[drop_indices, 'IsFraud'] = 0

# SAVE
df.to_csv('credit_card_fraud_dataset.csv', index=False)
print("SUCCESS: 'credit_card_fraud_dataset.csv' generated with 100,000 rows.")