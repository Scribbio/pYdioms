#Pick two distinct synsets and explore the concepts of hyponyms and hypernyms using WordNet

# A hyponym is a word of a more specific meaning than a more generic word such as bat,
# which we explored in the introduction section of our previous recipe.
# What we mean by more specific is, for example, cricket bat, baseball bat, carnivorous bat, squash racket, and so on.
# These are more specific in terms of communicating what exactly we are trying to mean.
# As opposed to a hyponym, a hypernym is a more general form or word of the same concept.
# For our example, bat is a more generic word and it could mean club, stick, artifact, mammal, animal, or organism.
# We can go as generic as the physical entity, living thing, or object and still be considered as a hypernym of the word bat.



from nltk.corpus import wordnet as wn

woman = wn.synset('woman.n.02')
bed = wn.synset('bed.n.01')


print(woman.hypernyms())
woman_paths = woman.hypernym_paths()

for idx, path in enumerate(woman_paths):
    print('\n\nHypernym Path :', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end='')

types_of_beds = bed.hyponyms()
print('\n\nTypes of beds(Hyponyms): ', types_of_beds)

print(sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas())))



