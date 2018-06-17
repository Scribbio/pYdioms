from nltk.corpus import CategorizedPlaintextCorpusReader
import nltk, string, numpy

reader = CategorizedPlaintextCorpusReader(r'\Users\JoeDi\Desktop\MSC\Idioms Corpera', r'.*\.txt', cat_pattern=r'(\w+)/*')

print(reader.categories())
print(reader.fileids())


from random import randint

File = reader.fileids()

fileP = File[randint(0, len(File)-1)]
print(fileP)

for w in reader.words(fileP):
    print(w + ' ', end='')
    if (w is '.'):
        print()

#https://sites.temple.edu/tudsc/2017/03/30/measuring-similarity-between-texts-in-python/

from sklearn.feature_extraction.text import CountVectorizer
import nltk, string, numpy

sss = "Because there is no easy way to decide how two words, two documents are related. All we have is sequence of letters " \
      "or strings if you prefer. So how to find a relationship between two words? If you want to decide how two documents related, " \
      "how to figure that out? It cant be done without having any other data."

sss2 = " If you want to decide how two documents related, how to figure that out? It cant be done without having any other data." \
       "If you have some other parameter, it can be converted into plot or statistical methods can be applied. " \
       "In order to create that parameter, document is first vectorized."

documents = [sss, sss2]



