import pandas as pd

def read_file_and_get_data():
    data = pd.read_csv(r'PathToFile\P6_Sentiment_Analysis_Tweets.csv')
    data["Sentiment"].value_counts()
    data.drop(['Unnamed: 0', 'ItemID'],axis=1,inplace=True)
    data.columns = ['label','text']

    return data