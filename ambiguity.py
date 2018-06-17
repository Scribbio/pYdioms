from nltk.corpus import wordnet as wn

#create string variable
chair = 'chair'

#Take an ambiguous word and explore all its senses using WordNet



chair_synsets = wn.synsets(chair)
print('Synsets/Senses of Chair :', chair_synsets, '\n\n')


#We are iterating over the list of synsets and printing the definition of each sense, associated lemmas/synonymous words,
# and example usage of each of the senses in a sentence. One typical iteration will print something similar to this:

for synset in chair_synsets:
    print(synset, ': ')
    print('Definition: ', synset.definition())
    print('Lemmas/Synonymous words: ', synset.lemma_names())
    print('Example: ', synset.examples(), '\n')


# As you can see, definitions, Lemmas, and example sentences of all seven senses of the word chair are seen in the output.
# Straightforward API interfaces are available for each of the operations as elaborated in the preceding code sample.
# Now, let's talk a little bit about how WordNet arrives at such conclusions.
# WordNet is a database of words that stores all information about them in a hierarchical manner.
# If we take a look at the current example Write about synsets and hierarchical nature of WordNet storage.
# The following diagram will explain it in more detail.