d1 = "It's easy I'm afraid"
d2 = "Can’t you speak? (Usually said to embarrass the other person). I just saw you kissing my boyfriend. What’s the matter? Cat got your tongue?"
d3 = "Not as easy as it appears to be. You want me to come to work at 6:00 AM? Easier said than done!"
d4 = "You can find good in every bad situation. Even though you just got fired, remember that every cloud has a silver lining – at least you don’t have to work for that grouchy boss anymore!"
documents = [d1, d2, d3, d4]

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





