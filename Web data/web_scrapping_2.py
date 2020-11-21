import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
# For webpages with https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter - ')
#print('First:', url)


count = input('Enter count: ')
count = int(count)

pos = input('Enter position: ')
pos = int(pos)
pos = pos-1

for i in range(count):
    urls = list()
    html = urllib.request.urlopen(url, context=ctx).read()
    #print('HTML',html)
    soup = BeautifulSoup(html, 'html.parser') # Clean HTML
    #print('SOUP', soup)
   
    tags = soup('a')
    for tag in tags:
        url = tag.get('href', None)
        urls.append(url)
    url = urls[pos]
    print('Retrieving', urls[pos])

data = urls[pos]
at_pos = data.find('known_by_')
space_pos = data.find('.html',at_pos) 
host = data[at_pos+9:space_pos]
print(host)


        

    

    
    
        
        



