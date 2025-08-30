import sys

sys.path.insert(1, r'C:\Users\MacPavel\Desktop\Eva_test\ass4\lab')
import rest_service
import normalization_functions 
import spacy_service

url = "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F"

article = rest_service.url_to_string(url)

clean_text = normalization_functions.clean_text(article)
normalized_text = normalization_functions.normalization(clean_text, "lemmatizing", "russian")

pos_doc = spacy_service.pos_defining(normalized_text)
counted_most_common_nouns_and_verbs = spacy_service.obtain_most_common_nouns_and_verbs(pos_doc)
most_common_named_types_entity = spacy_service.obtain_most_common_named_entity_types(pos_doc)
most_common_named_entities = spacy_service.obtain_most_common_named_entities(pos_doc)

print(counted_most_common_nouns_and_verbs)
print(most_common_named_entity_types)
print(most_common_named_entities)
