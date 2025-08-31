import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from logger import ProjectLogger

class Visualize:
    def __init__(self):
        self.PLogger=ProjectLogger()
        self.PLogger.info("Visualize initialized")
        
        self.df_trans=pd.read_csv("./data/transactions_with_revenue.csv")
        self.df_sentiment=pd.read_csv("./data/reviews_with_sentiment.csv")
        self.df_prod=pd.read_csv("./data/products.csv")
        #self.df_cust=pd.read_csv("./data/customers.csv")
        

    def Pro_Revenue_trend(self):
        """
        Plot a line graph of revenue over time.

        This function takes in no parameters and plots a line graph of the total revenue
        over time. The x-axis is the transaction date and the y-axis is the total revenue.
        The function also writes a log message indicating that the plot has been created.
        """
        plt.plot(self.df_trans['transaction_date'], self.df_trans['total_revenue'])
        plt.show()
        self.PLogger.info("plot diagram created")
    def Pro_Revenue_Bar(self):
        """
        Plot a bar chart of the average sentiment of each product.

        This function takes in no parameters and plots a bar chart of the average sentiment
        of each product. The x-axis is the average sentiment and the y-axis is the product name.
        The function also writes a log message indicating that the plot has been created.
        """
        
        avg_sentiment = self.df_sentiment.groupby('name')['polarity'].mean().sort_values()

# Step 2: Plot the bar chart
        #plt.figure(figsize=(10, 6))
        avg_sentiment.plot(kind='barh', color='skyblue')
       # plt.bar(self.df_trans['name'],self.df_trans['total_revenue'])
        #plt.title("Product Revenue Count")
       # plt.xlabel("name")
       # plt.ylabel("total_revenue")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        self.PLogger.info("Bar diagram created")

    def Pro_Revenue_Boxplot(self):
        #self.df_trans.boxplot(column='total_revenue', by='category')               df_grouped = df.groupby('name')['total_revenue'].sum().reset_index()
    """
    Plot a boxplot of total revenue by product name.

    This function groups the transaction data by product name and calculates the total revenue
    for each product. It then creates a boxplot to visualize the distribution of total revenue
    for each product. The function also writes a log message indicating that the boxplot has
    been created.
    """

        df_grouped = self.df_trans.groupby('name')['total_revenue'].sum().reset_index()
        print(df_grouped.head())
        df_grouped.boxplot(column='total_revenue', by='name')
        plt.show()
        self.PLogger.info("Boxplot diagram created")

    def Pro_Revenue_Pie(self):
        
        """
        Plot a pie chart of total revenue by product name.

        This function groups the transaction data by product name and calculates the total revenue
        for each product. It then creates a pie chart to visualize the distribution of total revenue
        for each product. The function also writes a log message indicating that the pie chart has
        been created.
        """
        self.df_trans['name'].value_counts().plot.pie(autopct='%1.1f%%')
        self.PLogger.info("Pie diagram created")
        plt.show()
if __name__=="__main__":
    Vis=Visualize()
    Vis.Pro_Revenue_trend()
    Vis.Pro_Revenue_Bar()
    Vis.Pro_Revenue_Boxplot()
    Vis.Pro_Revenue_Pie()