# n-grams, 2-grams
# Ghazal


text = "I am learning about n-grams"
ngrams = []
for i in range(len(text)-1):
    ngrams.append(text[i:i+2])           #stop is up to but not including
print(ngrams)


'''
text[i:i+2] is using the slicing technique of python to extract a substring from the text variable.
The i variable keeps track of the current position of the loop and i+2 is the next character of the current character. 
So in each iteration,
the loop is taking the current character and the next character and combining them
to form a 2-character substring, which is a bigram.
'''

'''
the slicing syntax in Python is typically start:stop:step,
where start is the index of the first element to be included in the slice, stop is the index of the first element that is excluded from the slice, and step is the number of indices between slice elements.

In this case, i is being used as the start index, and i+2 is being used as the stop index. The step is not being specified, so it defaults to 1.

When the for loop iterates, i is starting at 0 and the stop index is i+2 which is the index of the next character after the current character.
So, with each iteration, the loop is slicing the string text from the current character to the next character, resulting in a bigram.

It's worth noting that the stop index is not included in the slice, which is why the loop ends at len(text)-1. If it ends on len(text), the last bigram would be an empty string.

'''
