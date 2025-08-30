import imp
import sys

sys.path.insert(1, r'PathToFolder\ass6\lab')

import pandas_service
import normalization_functions
import feature_engineering_service
import modeling_service

data = pandas_service.read_file_and_get_data()

data['clean_text'] = data['text'].apply(lambda row : normalization_functions.clean_text(row))
data['final_text'] = data['clean_text'].apply(lambda row : normalization_functions.normalization(row, "stemming"))
data['punct%'] = data['text'].apply(lambda x: feature_engineering_service.count_punct(x))

bow_data = feature_engineering_service.get_bow_data(data)
data = feature_engineering_service.count_text_len(data)
# final_data = feature_engineering_service.get_final_data(data, bow_data)

modeling_service.build_classification(bow_data, data)