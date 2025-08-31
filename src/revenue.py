import os
import pandas as pd

class revenue:
    def __init__(self):
        self.df=pd.read_csv("./data/transactions.csv")
        self.df_pro=pd.read_csv("./data/products.csv")

    def total_revenue(self):
        """
        Calculate total revenue for each transaction and merge with product data.

        Multiply the price and quantity columns to calculate the total revenue for each
        transaction. Convert the product_id columns of both the transaction and product data
        to strings before merging them on product_id. The resulting DataFrame is returned.
        """
        
        
        self.df['total_revenue']=self.df['price']*self.df['quantity']
        self.df['product_id']=self.df['product_id'].astype(str)
        self.df_pro['product_id']=self.df_pro['product_id'].astype(str)
        print(self.df['product_id'].dtypes)
        print(self.df_pro['product_id'].dtypes)
        self.df=self.df.merge(self.df_pro, on='product_id', how='inner')
        return self.df
    def write_csv(self,filename):
    """
    Write the DataFrame to a CSV file.

    This function takes a filename as input and writes the DataFrame `self.df` to a CSV file
    with the specified filename in the "./data/" directory. The index is not included in the
    output file. The function returns the DataFrame after writing it to the file.

    :param filename: The name of the file to write the DataFrame to (without extension).
    :return: The DataFrame that was written to the CSV file.
    """

        self.df.to_csv("./data/"+f"{filename}"+".csv",index=False)
        return self.df
    
if __name__=="__main__":
    revenue_sample=revenue()
    revenue_sample.total_revenue()
    revenue_sample.write_csv("transactions_with_revenue")