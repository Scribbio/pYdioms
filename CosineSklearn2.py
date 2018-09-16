from nltk.corpus import CategorizedPlaintextCorpusReader
import ProcessText

d1 = "judge people by what they say"

d1_processed = ProcessText.ProcessText.process(d1)

documents = [d1]

#Read documents
reader = CategorizedPlaintextCorpusReader(r'\Users\JoeDi\Desktop\MSC\Idioms Corpera', r'.*\.txt', cat_pattern=r'(\w+)/*')

for w in reader.fileids():
    wd = reader.raw(w)
    documents.append(w + " " + wd)

print("Documents in the collection are: ")
print(documents)
print("\n")

from sklearn.feature_extraction.text import TfidfVectorizer

#build a TF/IDF matrix for each description
tfidf = TfidfVectorizer().fit_transform(documents)

print("Tf-idf weightings are:  ")
print(tfidf)
print("\n")

#code that will find us the top similar descriptions based on cosine similarity between the values in the matrix:
from sklearn.metrics.pairwise import linear_kernel
cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()

print("cosine_similarities: ")
print(cosine_similarities)
print("\n")

#return the second closest value (essentially this function sorts the similarities and returns the second highest)
match = sorted(set(cosine_similarities))[-2]

#iterate through list of similarites to find the position of our "match" in the list
pos = 0
for c in cosine_similarities:
    if c != match :
        pos+=1
    else:
        break

#position is obtained, return it's value from list of documents
print("Best match is: ", documents[pos])


########################################################################################################################





