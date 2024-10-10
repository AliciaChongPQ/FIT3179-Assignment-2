import pandas as pd  
df = pd.read_csv("FIT3179-Assignment-2\Disease_ages.csv")
print(df)
df["normalised_incidence"] = df["total_occurrence"] / df["population"]
df.to_csv('FIT3179-Assignment-2\Disease_ages.csv', index=False)
