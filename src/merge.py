import pandas as pd

class MergeData:
    def __init__(self):
        #self.df_trans=pd.read_csv("./data/transactions.csv")
        #self.df_cust=pd.read_csv("./data/customers.csv")   
        """
        Initialize the mergedata object by reading the four csv files into pandas DataFrames:
        transactions_with_revenue, reviews_with_sentiment, and products. These DataFrames are stored as
        instance variables of the class.
        """
        self.df_prod=pd.read_csv("./data/products.csv")
        self.trans_rev=pd.read_csv("./data/transactions_with_revenue.csv")
        self.df_rev=pd.read_csv("./data/reviews_with_sentiment.csv")
    def merge(self):
        return self.df_prod.merge(self.df_rev,how='inner',on='product_id').merge(self.trans_rev,how='inner',on='product_id')
if __name__=="__main__":
    merge=mergedata()
    print(merge.merge())