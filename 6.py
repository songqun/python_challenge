import re
import io
import zipfile
import urllib.request

url="http://www.pythonchallenge.com/pc/def/channel.zip"
data=io.BytesIO(urllib.request.urlopen(url).read())
file=zipfile.ZipFile(data)
num=90052

cmt=[]

while 1:
	text=file.read("%s.txt"%num).decode('ascii')
	match=re.search('Next nothing is (\d+)', text)
	cmt.append(file.getinfo("%s.txt"%num).comment.decode('ascii'))
	if match!=None:
		num=match.group(1)
	else:
		print(text)
		print("".join(cmt))
		break