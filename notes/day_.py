import pandas as pd

seattle = "https://raw.githubusercontent.com/nixwebb/CSV_Data/refs/heads/master/Seattle2014.csv"

data = pd.read_csv(seattle)

print("Greatest rainfall:", data["PRCP"].max())
print("Average rainfall:", data["PRCP"].mean())
print("Smallest rainfall:", data["PRCP"].min())
