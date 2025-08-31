# readSql.py

import pandas as pd
from db_config import sql_engine

class ReadSql:
    def __init__(self, tablename):
        """
        Automatically read data from the SQL table on initialization.
        """
        self.tablename = tablename
        self.df = pd.read_sql(f"SELECT * FROM {tablename}", con=sql_engine())

    def get_df(self):
        return self.df

