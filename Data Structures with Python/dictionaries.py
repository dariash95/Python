# Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

fhandle = open('mbox-short.txt')
counts = dict()
emails = list()

for line in fhandle:
    line = line.rstrip()

    if line.startswith('From'):
        if line.endswith('8'):
            email_lines = line.split()
            email = email_lines[1]
            emails.append(email)
            
for email in emails:
    counts[email] = counts.get(email,0) + 1

max_count = None
max_email = None

for email, count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(max_email,max_count)
