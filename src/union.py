import pandas as pd

class union_all:
    def __init__(self):
        """
        Initializes the union_all object by reading the four csv files into pandas DataFrames:
        transactions, customers, products, and product_reviews. These DataFrames are stored as
        instance variables of the class.
        """
        
        self.df_trans=pd.read_csv("./data/transactions.csv")
        self.df_cust=pd.read_csv("./data/customers.csv")   
        self.df_prod=pd.read_csv("./data/products.csv")
        self.df_rev=pd.read_csv("./data/product_reviews.csv")
    def union(self):
        """
        This function returns a pandas DataFrame that is the union of the four input
        csv files. The union is performed along the columns (axis=1). The function
        reads the four csv files into pandas DataFrames and concatenates them into
        a single DataFrame. The resulting DataFrame is returned by the function.

        Returns
        -------
        df : pandas.DataFrame
            The union of the four input csv files.

        """
        self.df=pd.concat([self.df_trans, self.df_cust,self.df_prod,self.df_rev], axis=1)
        return self.df
if __name__=="__main__":
    union_all=union_all()
    print(union_all.union())
    union_all.df.to_csv("./data/union.csv",index=False)
