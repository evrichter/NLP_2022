from sklearn.feature_extraction.text import CountVectorizer

import pandas
import string

def get_bow_data(data):
    bow_model = CountVectorizer()
    bow_vec = bow_model.fit_transform(data.final_text)
    bow_data = pandas.DataFrame(bow_vec.toarray(), columns = bow_model.get_feature_names())

    return bow_data

def count_text_len(data):
    data['text_len'] = data['text'].apply(lambda x: len(x) - x.count(" "))

    return data

def count_punct(text):
    count = sum([1 for char in text if char in string.punctuation])
    return round(count/(len(text) - text.count(" ")), 3)*100

def get_final_data(data, bow_data):
    final_data = pandas.concat([data['punct%'], data['text_len'], bow_data],axis=1)

    return final_data
