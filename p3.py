# Automated CSV File Inspector and Data Exporter
import pandas as pd

data = pd.read_csv("txt.csv")

print("\n---structural dimensions---")
rows, columns = data.shape
print("No. of rows = ", rows)
print("No. of columns = ", columns)

print("\n---summary data types---")
print(data.dtypes)

print("\n---analyze numerical standard---")
print(data.describe())

print("\n---filtering rows---")
filtered_data = data[data["Marks"] > 80]
print(filtered_data)

filtered_data.to_csv("filtered_data.csv", index=False)
print("\nFiltered data successfully saved to filtered_data.csv\n")