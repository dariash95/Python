fhandle = open('mbox-short.txt')

cont = 0
for line in fhandle:
    line = line.rstrip()     

    if line.startswith('From'):
        if line.endswith('8'):
            cont = cont+1
            mails = line.split()
            emails = mails[1]
            print(emails)
print('There were', cont, 'lines in the file with From as the first word')
    
