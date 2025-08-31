from textblob import TextBlob
import pandas as pd
from pandas_cleaning import clean

class Sentiment:
    def __init__(self):
        self.df=pd.read_csv(".\data\product_reviews.csv")
        self.df_prod=pd.read_csv(".\data\products.csv")
        self.df_sent=self.df.merge(self.df_prod, on='product_id', how='inner')
        clean_data=clean(self.df_sent)
        clean_data.remove_nan()
        clean_data.remove_duplicates()
        clean_data.fix_nulls(0)
        
    def get_sentiment(self,text):
        """
    Given a text string, return:
    - polarity: sentiment score from -1 (negative) to +1 (positive)
    - subjectivity: how opinion-based the text is (0 = factual, 1 = opinion)
    """

        blob=TextBlob(str(text))
        return pd.Series([blob.sentiment.polarity, blob.sentiment.subjectivity])
    def add_sentiment(self):
    """
    Analyze sentiment of review text and add polarity and subjectivity columns.

    This method applies sentiment analysis to the 'review_text' column of the DataFrame
    to compute polarity and subjectivity scores. The results are added as new columns
    'polarity' and 'subjectivity' to the DataFrame.

    Returns:
    pd.DataFrame: The DataFrame with added sentiment analysis columns.
    """

        self.df_sent[['polarity','subjectivity']]=self.df_sent['review_text'].apply(self.get_sentiment)
        return self.df_sent

    def set_lable(self,polarity):
        """
        Categorize sentiment based on polarity:
        - Positive: polarity > 0.1
        - Negative: polarity < -0.1
        - Neutral: everything else
        """
        if polarity > 0.1:
            return "positive"
        elif polarity < -0.1:
            return "negative"
        else:
            return "neutral"
        return label_sentiment
    def add_lable(self):
        self.df_sent['sentiment']=self.df_sent['polarity'].apply(self.set_lable)
        return self.df_sent

if __name__=="__main__":
    sentiment_sample=Sentiment()
    sentiment_sample.add_sentiment()
    sentiment_sample.add_lable()
    
# Optional: Save the results to a new CSV file
    sentiment_sample.df_sent.to_csv("./data/reviews_with_sentiment.csv", index=False)

