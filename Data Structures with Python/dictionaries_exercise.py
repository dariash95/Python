counts = dict()
print('Enter a line of the text:')
line = input('')

words = line.split()

# Counting
for word in words:
    counts[words] = counts.get(word,0) + 1

print('Counts', counts)

# The general pattern to count the words in a line is to split the line into
# words and then loop through the words and use a dictionary to track the count
# each word independently 
