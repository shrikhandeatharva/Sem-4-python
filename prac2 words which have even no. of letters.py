sentence = "print only the word that starts with s in this sentence"

# Split the sentence into words
words = sentence.split()
print(words)
print(type(words))
print('The words having even number of letters starting with s are : ')

# Iterate over each word and print those with even number of letters starting with s 
for word in words:
    if (len(word) % 2 == 0 and word.lower().startswith('s') ):
        print(word)
