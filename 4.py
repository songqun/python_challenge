import urllib.request
import re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num="12345"

while 1:
	text=urllib.request.urlopen(url+num).read().decode('ascii')
	match=re.search('and the next nothing is (\d+)', text)
	if match!=None:
		num=match.group(1)
	else:
		print(num)
		break

num="8022"

while 1:
	text=urllib.request.urlopen(url+num).read().decode('ascii')
	match=re.search('and the next nothing is (\d+)', text)
	if match!=None:
		num=match.group(1)
	else:
		print(num)
		break