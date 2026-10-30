import pandas as pd

print("1. Loading dataset...")
df = pd.read_csv('Amazon.csv')

print(f"2. Dataset loaded successfully! Total rows: {len(df)}")
print("Columns in dataset:", list(df.columns[:5]), "...")

print("3. Cleaning dates and dropping duplicates...")
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
df = df.drop_duplicates(subset=['OrderID'])

print("4. Extracting Year and Month features...")
df['Year'] = df['OrderDate'].dt.year
df['Month_Name'] = df['OrderDate'].dt.strftime('%B')

df = df.dropna(subset=['OrderID', 'OrderDate'])

print("5. Saving cleaned file...")
df.to_csv('amazon_cleaned.csv', index=False)

print(f"SUCCESS! Cleaned file saved as 'amazon_cleaned.csv' with {len(df)} rows.")