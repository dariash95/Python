fname = input('Enter file name: ')
try: 
	fh = open(fname)
except:
    print('Please enter a valid file name')
    quit()
    
for line in fh:
    line = line.strip()
    line = line.upper()
    print(line)
