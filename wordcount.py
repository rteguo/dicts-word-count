"""Count words in file."""


# put your code here.
input_file = open("test.txt")
word_counts_char = {}

# Loop on the file
for line in input_file:
    #Remove Remove trailing whitespace at the end of each line
    line = line.rstrip()

    #Move all the non aphabetic character
    line = line.replace(".", " ")
    line = line.replace("?", " ")

    #Split the line by space to get a list of words
    words = line.split()

    # Loop on the list of word for any line
    for word in words:
        word_counts_char[word] = word_counts_char.get(word, 0) + 1

#Print the words with number of items
for word, count in word_counts_char.items():
    print(f'{word} {count}')


