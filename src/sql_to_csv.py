import pandas as pd
import os
from db_config import sql_engine

class sql_csv:
    def __init__(self,tablename):
    """
    Initializes the sql_csv class with the given table name, retrieves data from the SQL table, 
    and saves it as a CSV file in the data directory.

    Parameters:
    tablename (str): The name of the SQL table to be read and converted to CSV.
    """

        engine=sql_engine()
        query=f"SELECT * FROM {tablename}"
        table=pd.read_sql(query,con=engine)
  
        return table.to_csv("./data/"+f"{tablename}"+".csv",index=False)        
if __name__=="__main__":
    sql_csv("customers")