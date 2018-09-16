#Compute the average polysemy of nouns, verbs, adjectives, and adverbs according to WordNet

# First, let's understand what polysemy is. Polysemy means many possible meanings of a word or a phrase.
# As we have already seen, English is an ambiguous language and more than one meaning usually exists
# for most of the words in the hierarchy. Now, turning back our attention to the problem statement,
# we must calculate the average polysemy based on specific linguistic properties of all words in WordNet.
# As we'll see, this recipe is different from previous recipes. It's not just an API concept discovery
# but we are going to discover a linguistic concept here
# (I'm all emotional to finally get a chance to do so in this chapter.


from nltk.corpus import wordnet as wn

type = 'n' #n = nouns


synsets = wn.all_synsets(type)

lemmas = []

for synset in synsets:
    for lemma in synset.lemmas():
          lemmas.append(lemma.name())

#emove the duplicates and take the count of distinct lemmas:
lemmas = set(lemmas)

count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type))

print('Total distinct lemmas: ', len(lemmas))
print('Total senses :',count)
print('Average Polysemy of ', type,': ' , count/len(lemmas))
