import pandas as pd
import re, nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer



# ----------------------------
# Start Classification Process
# ----------------------------

def text_clean(corpus, keep_list):
    cleaned_corpus = pd.Series()
    for row in corpus:
        qs = []
        for word in row.split():
            if word not in keep_list:
                p1 = re.sub(pattern='[^a-zA-Z0-9]',repl=' ',string=word)
                #p1 = p1.decode('utf-8', 'ignore')
                p1 = p1.lower()
                qs.append(p1)
            else : qs.append(word)
        cleaned_corpus = cleaned_corpus.append(pd.Series(' '.join(qs)))
    return cleaned_corpus


def preprocess(corpus, keep_list, cleaning = True, stemming = False, stem_type = None, lemmatization = False, remove_stopwords = True):
    
    if cleaning == True:
        corpus = text_clean(corpus, keep_list)

    if remove_stopwords == True:
        wh_words = ['who', 'what', 'when', 'why', 'how', 'which', 'where', 'whom']
        stop = set(stopwords.words('english'))
        for word in wh_words:
            stop.remove(word)
        corpus = [[x for x in x.split() if x not in stop] for x in corpus]
    else :
        corpus = [[x for x in x.split()] for x in corpus]

    if lemmatization == True:
        lem = WordNetLemmatizer()
        corpus = [[lem.lemmatize(x, pos = 'v') for x in x] for x in corpus]

    if stemming == True:
        if stem_type == 'snowball':
            stemmer = SnowballStemmer(language = 'english')
            corpus = [[stemmer.stem(x) for x in x] for x in corpus]
        else :
            stemmer = PorterStemmer()
            corpus = [[stemmer.stem(x) for x in x] for x in corpus]

    corpus = [' '.join(x) for x in corpus]
    return corpus

# ----------------------------
# End Classification Process
# ----------------------------