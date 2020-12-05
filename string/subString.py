#This code checks if a string contains a partiticular substring
def subString(sub, str):
    if sub in str:
        print(f'{str} contains {sub}')
    else:
        print(f'{str} does not contain {sub}')

subString('nima', 'nimnnjsndsnnimannnima')

#find() and count()

def firstOccur(sub, str):
    print(str.find(sub))  # returns -1
    print(str.index(sub)) # returns ValueError

firstOccur('nima', 'nimnnjsndsnnimannnima')

story = 'The price is right said Bob. The price is right.'
print(story.rfind('is')) #rfind() finds like find() but from right


#Replace all instances of a substring in a string
sentence = 'Sally sells sea shells by the sea shore'
print(sentence.replace('sea', 'mountain'))


print(min('nadnvins'))



sentence = "If you want to be a ninja"
print(sentence.partition(' want '))

""" partition() splits a string on the first 
instance of a substring. A tuple of the split
string is returned without the substring removed """