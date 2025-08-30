import sys

sys.path.insert(1, r'C:\Users\file_path')

import pandas_service
import relation_pattern_service
import spacy_service
import graph_service

data = pandas_service.read_file_and_get_data()

data['sentence_processed'] = spacy_service.apply_nlp(data)

entity_pairs = relation_pattern_service.get_entity_pairs(data)
relations = relation_pattern_service.get_relations(data)

kg_df = pandas_service.create_dataframe(entity_pairs, relations)

graph_service.plot_network(kg_df)