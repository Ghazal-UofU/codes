# n-grams, 2-grams
# Ghazal


text = "I am learning about n-grams"
ngrams = []
for i in range(len(text)-1):
    ngrams.append(text[i:i+2])
print(ngrams)
