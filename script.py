import pandas as pd

df = pd.read_csv("Sample-Superstore.csv", encoding='ISO-8859-1')

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')

# Reformat to 'DD/MM/YYYY'
df['Order Date'] = df['Order Date'].dt.strftime('%d/%m/%Y')
df['Ship Date'] = df['Ship Date'].dt.strftime('%d/%m/%Y')

# Save the cleaned dataset
df.to_csv("Superstore_Sales_Cleaned.csv", index=False)

print("Date format converted and file saved as Superstore_Sales_Cleaned.csv")