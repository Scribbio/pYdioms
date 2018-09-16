from nltk.corpus import reuters

words16097 = reuters.words(['test/16097'])
print(words16097)

words20 = reuters.words(['test/16097'])[:20]
print(words20)


#the reuters corpus is not just a list of files but is also hierarchically categorized
# into 90 topics. Each topic has many files associated with it.
# What this means is that, when you access any one of the topics,
# you are actually accessing the set of all files associated with that topic.
# Let's first output the list of topics by adding the following code:

reutersGenres = reuters.categories()
print(reutersGenres)

for w in reuters.words(categories=['bop','cocoa']):
    print(w+' ',end='')
    if(w is '.'):
        print()




