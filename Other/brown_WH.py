#Counting all the wh (question words) words in three different genres in the Brown corpus

# The Brown corpus is part of the NLTK data package. It's one of the oldest text corpuses assembled at Brown University.
# It contains a collection of 500 texts broadly categorized in to 15 different
# genres/categories such as news, humor, religion, and so on.

import nltk
from nltk.corpus import brown

print(brown.categories())

genres = ['fiction', 'humor', 'romance']
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']

for i in range(0,len(genres)):genre = genres[i]
print()
print("Analysing '"+ genre + "' wh words")
genre_text = brown.words(categories = genre)

fdist = nltk.FreqDist(genre_text)

for wh in whwords:
    print(wh + ':', fdist[wh], end=' ')
