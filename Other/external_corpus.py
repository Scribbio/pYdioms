#Downloading an external corpus, load it, and access it

from nltk.corpus import CategorizedPlaintextCorpusReader
from random import randint #random

# The first line is where you are reading the corpus by calling
# the CategorizedPlaintextCorpusReader constructor.
# The three arguments from left to right are Absolute Path
# to the folder containing the corpus on your computer, all sample
# document names from the txt_sentoken folder, and the categories
# in the given corpus (in our case, 'pos' and 'neg'

reader = CategorizedPlaintextCorpusReader(r'\Users\JoeDi\Desktop\python projs\tokens', r'.*\.txt', cat_pattern=r'(\w+)/*')


print(reader.categories())
print(reader.fileids())

# Now that we've made sure that the corpus is loaded correctly, let's
# get on with accessing any one of the sample documents from both the categories.
# For that, let's first create a list, each containing samples of both the categories, 'pos' and 'neg', respectively.
# Add the following two lines of code:

posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')

# The next two files select a random file, each from the set of positive
# and negative category reviews. The last two lines just print the filenames.

fileP = posFiles[randint(0,len(posFiles)-1)]
fileN = negFiles[randint(0, len(posFiles) - 1)]
print(fileP)
print(fileN)

# Now that we have selected the two files, let 's access them and print

for w in reader.words(fileP):
    print(w + ' ', end='')
    if (w is '.'):
        print()
        for w in reader.words(fileN):
            print(w + ' ', end='')
            if (w is '.'):
                print()


#How it works...
#The quintessential ingredient of this recipe is the CategorizedPlaintextCorpusReader class of NLTK.
# Since we already know that the corpus we have downloaded is categorized, we only need provide
# appropriate arguments when creating the reader object.
# The implementation of the CategorizedPlaintextCorpusReader class
# internally takes care of loading the samples in appropriate buckets ('pos' and 'neg' in this case).