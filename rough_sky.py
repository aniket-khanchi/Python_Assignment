import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    print( row["x"],row['y'])