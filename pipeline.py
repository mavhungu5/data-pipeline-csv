import pandas as pd
import sqlite3

# STEP 1: Extract (Load CSV)
df = pd.read_csv("superstore.csv")

# STEP 2: Transform (Clean data)
df = df.dropna()  # remove missing values

# Convert column names to lowercase (clean structure)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# STEP 3: Load (Save to SQLite)
conn = sqlite3.connect("pipeline.db")

df.to_sql("clean_orders", conn, if_exists="replace", index=False)

print("Data pipeline executed successfully!")