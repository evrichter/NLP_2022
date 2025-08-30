import nltk

import spacy
from spacy.lang.ru.examples import sentences

from collections import Counter

# nlp = spacy.load("ru_core_news_sm")
nlp = spacy.load("en_core_web_sm")

def pos_defining(text):
    pos_doc = nlp(text)

    return pos_doc

def apply_nlp(data):
    return data['sentence'].apply(nlp)

def get_bigrams(words_clean):
    return nltk.bigrams(words_clean)

def get_FreqDist(bigrams):
    return nltk.probability.FreqDist(bigrams)

def obtain_most_common_nouns_and_verbs(pos_doc):
    labels = []

    for token in pos_doc:
        label = token.text
        pos = token.pos_

        if (pos == "NOUN" or pos == "VERB"):
            labels.append(label)
    
    filtred_nouns_and_verbs = " ".join(labels)
    conted_most_common_nouns_and_verbs = Counter(filtred_nouns_and_verbs.split())

    return conted_most_common_nouns_and_verbs.most_common(20)

def obtain_most_common_named_entity_types(pos_doc):
    labels = []

    for token in pos_doc.ents:
        entity_type = token.label_

        labels.append(entity_type)
    
    string_of_entity_types = " ".join(labels)
    most_common_named_entity_types = Counter(string_of_entity_types.split())

    return most_common_named_entity_types.most_common(3)

def obtain_most_common_named_entities(pos_doc):
    labels = []

    for token in pos_doc.ents:
        named_entity = token.text

        labels.append(named_entity)
    
    string_of_named_entities = " ".join(labels)
    most_common_named_entities = Counter(string_of_named_entities.split())

    return most_common_named_entities.most_common(20)