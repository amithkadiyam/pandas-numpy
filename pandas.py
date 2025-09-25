import pandas as pd
data = {
    'CustomerID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'TotalPurchase' : [2500, 1800, 3200]
}

df = pd.DataFrame(data)
print(df)