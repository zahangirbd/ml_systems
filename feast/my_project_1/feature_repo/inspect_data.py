import pandas as pd
df = pd.read_parquet("data/driver_stats.parquet")
print(df.head())
#print(df)
df.to_csv('data/driver_stats.csv')