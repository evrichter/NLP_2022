import pandas as pd

def read_file_and_get_data():
    data = pd.read_fwf(r'C:\Users\MacPavel\Desktop\Eva_test\ass5\lab\P5_Wikipedia_Sentences_short.txt', header=None, names=["sentence"])

    return data

def find_series(relations):
    return pd.Series(relations).value_counts()[:50]

def create_dataframe(entity_pairs, relations):
    source = [i[0] for i in entity_pairs]

    target = [i[1] for i in entity_pairs]

    kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})

    return kg_df