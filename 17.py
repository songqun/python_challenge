import urllib.request
import re
import urllib.parse
import bz2
import xmlrpc.client

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
num="12345"
info=""
while 1:
	text1=urllib.request.urlopen(url+num).read().decode('ascii')
	match1=re.search('and the next busynothing is (\d+)', text1)
	text2=urllib.request.urlopen(url+num).getheader("Set-Cookie")
	info+=re.search('info=([^;]+);',text2).group(1)
	if match1!=None:
		num=match1.group(1)
	else:
		print(num)
		break
print(bz2.decompress(urllib.parse.unquote_to_bytes(info.replace("+", " "))).decode())

server=xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(server.phone("Leopold"))

message="the flowers are on their way"
url2="http://www.pythonchallenge.com/pc/stuff/violin.php"
request=urllib.request.Request(url2, headers={"Cookie": "info="+urllib.parse.quote_plus(message)})
print(urllib.request.urlopen(request).read().decode())