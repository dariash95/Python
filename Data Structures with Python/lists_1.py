# Open the file romeo.txt and read it line by line. For each line, split the
# line into a list of words using the split() method. The program should build
# a list of words.For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.

fhandle = open('romeo.txt')

words = list()
solution = list()

for text in fhandle:
     line = text.split()

     i = 0
     for i in range(len(line)):
         words.append(line[i])
         i = i+1

j = 0
for j in words:
     if j not in solution:
          solution.append(j)

solution.sort()
print(solution)



