import urllib.request
import io
import gzip
import difflib

url = "http://www.pythonchallenge.com/pc/return/deltas.gz"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/return/"
password_mgr.add_password(None, top_level_url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data = io.BytesIO(urllib.request.urlopen(url).read())

code=gzip.open(data)
col1=[]
col2=[]
for line in code:
	col1.append(line[0:53].decode())
	col2.append(line[56:-1].decode())

f1=open("18_rst1.jpg","wb")
f2=open("18_rst2.jpg","wb")
f3=open("18_rst3.jpg","wb")
compare=difflib.Differ().compare(col1,col2)
for line in compare:
	bs=bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
	if (line[0]=="+"):
		f1.write(bs)
	elif (line[0]=="-"):
		f2.write(bs)
	else:
		f3.write(bs)