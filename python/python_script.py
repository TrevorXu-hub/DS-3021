
import pandas as pd
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(data_url)
print(df.head())