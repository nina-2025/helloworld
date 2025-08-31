import pandas as pd
from pandas_cleaning   import clean
import os

class readPandas:
    def __init__(self):
        """
        Initializes the readPandas object by reading the four csv files into pandas DataFrames:
        transactions, customers, products, and product_reviews. These DataFrames are stored as
        instance variables of the class. It also performs some data cleaning operations on these
        DataFrames, such as renaming columns, removing NaN values, removing duplicates, converting
        columns to appropriate data types, and fixing null values.
        """
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        csv_files = [
                os.path.abspath(os.path.join(BASE_DIR, '..', 'data', 'products.csv')),
                os.path.abspath(os.path.join(BASE_DIR, '..', 'data', 'customers.csv')),
                os.path.abspath(os.path.join(BASE_DIR, '..', 'data', 'transactions.csv')),
                os.path.abspath(os.path.join(BASE_DIR, '..', 'data', 'product_reviews.csv'))

]
        for i in csv_files:
                
                df=pd.read_csv(i)
                self.df = df
                cleaning=clean(self.df)

            #  cleaning.readsql('transactions')
              #  cleaning.describe()
                cleaning.info()

                cleaning.rename_col('customer_id','CID')
                cleaning.rename_col('product_id','PID')
                print(df.columns)

               # cleaning.remove_nan()
                #cleaning.remove_duplicates()
                #clearcleaning.fix_nulls(0)
                #cleaning.int_convert()
                #cleaning.date_convert()
                #cleaning.str_convert()

    #def select_columns(self, columns):
     #   return self.df[columns]
            

if __name__ == "__main__":
    app=readPandas()
    