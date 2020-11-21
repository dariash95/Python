import re

list_values = list()
tot = 0

fhandle = open('regex.txt')
for line in fhandle:
    line = line.strip()
    value = re.findall('[0-9]+', line)
    if value == []:
        continue
    else:
        for i in range(len(value)):
            value[i] = int(value[i])
            tot = tot + value [i]
print(tot)
