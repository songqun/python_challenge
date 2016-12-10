import urllib.request
import io
import re

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

top_level_url = "http://www.pythonchallenge.com/pc/hex/"
password_mgr.add_password(None, top_level_url, "butter", "fly")
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
print(response.headers)

request=urllib.request.Request(url)
pattern=re.compile("bytes (\d+)-(\d+)/(\d+)")
content_range=response.headers["Content-Range"]
(begin, end, length)=pattern.search(content_range).groups()

while True:
	request.headers["Range"]="bytes=%i-" % (int(end)+1)
	try:
		response = urllib.request.urlopen(request)
	except:
		break
	print(response.read().decode())
	print(response.headers)
	content_range=response.headers["Content-Range"]
	(begin, end, length)=pattern.search(content_range).groups()

request.headers["Range"]="bytes=%i-" % (int(length)+1)
response = urllib.request.urlopen(request)
print(response.read().decode())
print(response.headers)
content_range=response.headers["Content-Range"]
(begin, end, length)=pattern.search(content_range).groups()

request.headers["Range"]="bytes=%i-" % (int(begin)-1)
response = urllib.request.urlopen(request)
print(response.read().decode())
print(response.headers)

request.headers["Range"]="bytes=1152983631-"
response = urllib.request.urlopen(request)

f=open("20_rst.zip","wb")
f.write(response.read())