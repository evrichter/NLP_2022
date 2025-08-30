import re
import nltk

import re
import nltk

def tokenize(text): # Takes a string as an input
    tokens = nltk.tokenize.word_tokenize(text) #  tokenize the text
    return tokens # Returns a list of tokens

def lower_case(tokens): # Takes a list of tokens as an input
    tokens_lower = [w.lower() for w in tokens] # lowercase the tokens
    return tokens_lower # Returns a list of lowercased tokens

def remove_punct(tokens):# Takes a list of tokens as an input
    tokens_nopunct = [token for token in tokens if token.isalpha()] # remove punctuation from the tokens
    return tokens_nopunct # Returns a list of words without punctuation

def remove_stopwords(tokens, language):# Takes a list of tokens and a language as an input
    stopwords = nltk.corpus.stopwords.words(language) # load stopwords
    tokens_nosw = [token for token in tokens if token not in stopwords] # remove stopwords from the tokens
    return tokens_nosw

def stemming(tokens):
    stemmer = nltk.PorterStemmer() # load stemmer
    tokens_stemmed = [stemmer.stem(word) for word in tokens] # TODO stem the tokens
    return(tokens_stemmed)

def lemmatizing(tokens):
    wn = nltk.WordNetLemmatizer() # load lemmatizer
    tokens_lemmatize = [wn.lemmatize(word) for word in tokens] # lemmatize the tokens
    return(tokens_lemmatize)

def clean_text(text,normalization): # A full function that performs all of the normalization steps
    # You can call functions described above from here
    tokens = tokenize(text) # 1. Tokenize
    tokens_lower = lower_case(tokens) # 2. Lowercase
    token_nopunct = remove_punct(tokens_lower) # 3. Punctuation removal
    tokens_nosw = remove_stopwords(tokens, "english") # 4. Stopwords removal (the language can also be an argument of the clean_text function)
    # 5. Create a IF to choose either stemming or lemmatization
    if normalization == "stemming":
        clean_tokens = stemming(tokens_nosw)
    else:
        clean_tokens = lemmatizing(tokens_nosw)
    # 6. Join the final token to return a clean text
    clean_text = " ".join(tokens)
    return (clean_text)