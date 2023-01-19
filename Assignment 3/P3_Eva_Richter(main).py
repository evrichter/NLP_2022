import sys

sys.path.insert(1, r'home/eva/Downloads: cleaning_functions.py')
from cleaning_functions import *

sentence = "It is a Truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife"

stemmed_words = clean_text(sentence, "stemming")
lemmatized_words = clean_text(sentence, "lemmatization")

print(stemmed_words)
print(lemmatized_words)