from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import PorterStemmer, LancasterStemmer, word_tokenize, WordNetLemmatizer
from nltk.corpus import gutenberg
import nltk
#refactor all these import staments!

class ProcessText:

    def __init__(self):
        return

    def process(txt):


        #preserves smilies
        tTokenizer = TweetTokenizer()
        tokenised = tTokenizer.tokenize(txt)

        #print('Tokenised: ', tokenised)

        #Remove punctuation
        noPunct = [e for e in tokenised if len(e) >= 3]

        # Remove stopwords
        stopwords = nltk.corpus.stopwords.words('english')
        words = [w for w in noPunct if w.lower() not in stopwords]
        print('Stopwords: ', words)

        #Lemmatise
        #removes prefixes: dis-, in-, re-, and suffixes: -ed, -ing, -ly, and -es
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(t) for t in words]
        print('Lemmatised: ', lemmas)

        return lemmas