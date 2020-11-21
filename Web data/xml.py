import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1041659.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()   
tree = ET.fromstring(data)

counts = tree.findall('comments/comment')

tot = 0
for item in counts:
    num = item.find('count').text
    num = int(num)
    tot = tot + num
print(tot)
