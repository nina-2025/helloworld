import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv('C:\Users\navaz\Desktop\Data_Analysis Project Files\Src_Data\customers.csv')
engine = create_engine("mysql+mysqlconnector://root:Mysql@2025@localhost/testdb")
df.to_sql('customers', con=engine, if_exists='append', index=False)

print("Data imported into MySQL database successfully.")