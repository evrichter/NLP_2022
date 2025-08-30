from tqdm import tqdm

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

def get_entities(sent):
    ent1 = ""
    ent2 = ""

    prv_tok_dep = ""
    prv_tok_text = ""

    prefix = ""
    modifier = ""

    for tok in sent:
        if tok.dep_ != "punct":
            if tok.dep_ == "compound":
                prefix = tok.text
                if prv_tok_dep == "compound":
                    prefix = prv_tok_text + " "+ tok.text
        
        if tok.dep_.endswith("mod") == True:
            modifier = tok.text
            if prv_tok_dep == "compound":
                modifier = prv_tok_text + " "+ tok.text
        
        if tok.dep_.find("subj") == True:
            ent1 = modifier +" "+ prefix + " "+ tok.text
            prefix = ""
            modifier = ""
            prv_tok_dep = ""
            prv_tok_text = ""      

        if tok.dep_.find("obj") == True:
            ent2 = modifier +" "+ prefix +" "+ tok.text
            
        prv_tok_dep = tok.dep_
        prv_tok_text = tok.text

    return [ent1.strip(), ent2.strip()]

def get_entity_pairs(sentences):
    entity_pairs = []

    for sent in tqdm(sentences["sentence_processed"]):
        entity_pairs.append(get_entities(sent))
    
    return entity_pairs

def get_relation(sent):
    matcher = Matcher(nlp.vocab)

    pattern = [[{'DEP':'ROOT'}, 
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},  
            {'POS':'ADJ','OP':"?"}]] 

    matcher.add("matching_1", pattern) 

    matches = matcher(sent)
    k = len(matches) - 1

    span = sent[matches[k][1]:matches[k][2]] 

    return(span.lemma_)

def get_relations(data):
    relations = [get_relation(i) for i in tqdm(data['sentence_processed'])]
    
    return relations