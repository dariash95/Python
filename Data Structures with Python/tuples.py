#  Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.

fhandle = open('mbox-short.txt')
hours = list()
list_aux = list()
counts = dict()

for line in fhandle:
    line = line.rstrip()

    if line.startswith('From'):
        if line.endswith('8'):
            email_lines = line.split()
            time = email_lines[5]
            aux = time.split(':')
            hour = aux[0]
            hours.append(hour)

for hour in hours:
    counts[hour] = counts.get(hour,0) + 1

for k,v in counts.items():
    new_tuple = (k,v)
    list_aux.append(new_tuple)

list_aux = sorted(list_aux)

for k,v in list_aux:
    print(k,v)
