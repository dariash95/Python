fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('Please enter a valid file name')
    quit()
cont = 0
tot = 0
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence: 0'):
        continue
    cont = cont + 1
    pos_0 = line.find('0')
    pos_5 = pos_0 + 5
    number = line[pos_0:pos_5+1]
    number = float(number)
    tot = tot + number

avg = tot/cont
print('Average spam confidence:',avg)

        
        
