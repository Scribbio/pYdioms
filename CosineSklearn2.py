####Adding Corpera

from nltk.corpus import CategorizedPlaintextCorpusReader


d1 = "I feel very nervous"

documents = [d1]

reader = CategorizedPlaintextCorpusReader(r'\Users\JoeDi\Desktop\MSC\Idioms Corpera', r'.*\.txt', cat_pattern=r'(\w+)/*')


for w in reader.fileids():
    wd = reader.raw(w)
    documents.append(w + " " + wd)

#print(documents)

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

tfidf = TfidfVectorizer().fit_transform(documents)

from sklearn.metrics.pairwise import linear_kernel
cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
print(cosine_similarities)

related_docs_indices = cosine_similarities.argsort()[:-3:-1]
print(cosine_similarities[related_docs_indices])

#print second highest value in array
match = sorted(set(cosine_similarities))[-2]

pos = 0

for c in cosine_similarities:
    if c != match :
        pos+=1
    else:
        break

print("Best match is: ", documents[pos])






#############################





