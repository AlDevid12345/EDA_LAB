import pandas as pd
df = pd.read_csv(r"D:\EDA_Lab\25EC01004\Lab1\Electrical Data\MOSFET_ID_VDS.csv")
print(df.columns, df.shape)
print(df.describe())