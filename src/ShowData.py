
from readSql import ReadSql
import os
from readCSV import readcsv

class showData:
    def __init__(self):
        """
        Prints out the data from the SQL tables and CSV files.

        This class is initialized with no parameters and prints out the data
        from the SQL tables named 'customers' and 'transactions' and from the
        CSV files named 'product.csv' and 'product_review.csv'.
        """
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        csv_files = [
                os.path.abspath(os.path.join(BASE_DIR, '..', 'data', 'products.csv')),
                os.path.abspath(os.path.join(BASE_DIR, '..', 'data', 'product_reviews.csv'))
]

        table_name = ["customers", "transactions"]
        for i in table_name:
           sql_pipe=ReadSql(i)
           print(sql_pipe.get_df())
        for j in csv_files :
            readcsv_file = readcsv(j)
            print(readcsv_file.get_csv())
          
if __name__ == '__main__' :
    showData()
