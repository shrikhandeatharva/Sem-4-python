sentence = "print only the word that starts with s in this sentence"

# Split the sentence into words
words = sentence.split()

# Print a message indicating the output
print('The words starting from s in the given sentence are:')

# Iterate over each word and print those that start with 's'
for word in words:
    if word.lower().startswith('s'):
        print(word)
