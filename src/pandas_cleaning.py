import pandas as pd
from db_config import sql_engine
class clean:
    def __init__(self, df):
        self.df = df

    def read_csv(self, filename):
        return self.df.read_csv(filename)
    def describe(self):
        return self.df.describe()
    def info(self):
        return self.df.info()

    def readsql(self, tablename):
        engine = sql_engine()  # Make sure this returns a SQLAlchemy engine
        query = f"SELECT * FROM {tablename}"
        return pd.read_sql(query, con=engine)
 
         
    def remove_nan(self):
        """
        Remove rows with missing values in the DataFrame.

        Returns:
        pd.DataFrame: DataFrame with rows containing missing values removed.
        It should be used with care
        """
        # Reset index after dropping
        #df.reset_index(drop=True, inplace=True)

        return self.df.dropna()

    def remove_duplicates(self):
        """
        Remove duplicate rows from the DataFrame.

        Returns:
        pd.DataFrame: DataFrame with duplicate rows removed.
        """
        return self.df.drop_duplicates()
    def fix_nulls(self,value):
       
        """
        Replace all null values with 0 in the DataFrame.

        Returns:
        pd.DataFrame: DataFrame with null values replaced with 0.
        """
        
        return self.df.fillna(value)
    def str_convert(self,col):
        """
        Convert the given column to string type.

        Returns:
        pd.Series: The converted column as string type.
        """
        df[col]=df[col].astype(str)
        return df[col]
    def date_convert(self ,col):
        """
        Convert the given column to datetime type.

        The errors parameter of the to_datetime method is set to 'coerce',
        which means that if the conversion fails, the resulting value will
        be NaT (Not a Time).

        Returns:
        pd.Series: The converted column as datetime type.
        """
        df[col]=df.to_datetime(df[col],errors='coerce')
        return df[col]
    def int_convert(self,col):
        """
        Convert the given column to numeric type.

        The errors parameter of the to_numeric method is set to 'coerce',
        which means that if the conversion fails, the resulting value will
        be NaN (Not a Number).

        Returns:
        pd.Series: The converted column as numeric type.
        """
        df[col]=df.to_numeric(df[col],errors='coerce')
        return df[col]
    def rename_col(self,oldname,newname):
        print(oldname+ "changed to "+newname)
        self.df.rename(columns={oldname: newname}, inplace=True)
