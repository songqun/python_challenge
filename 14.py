import urllib.request
import io
from PIL import Image

url = "http://www.pythonchallenge.com/pc/return/wire.png"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/return/"
password_mgr.add_password(None, top_level_url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data = io.BytesIO(urllib.request.urlopen(url).read())
im = Image.open(data)
newIm=Image.new(im.mode, (100,100))

curcood=[-1,0]
d=200
count=0

while d/2>1:
	step=d//2
	for s in range(step):
		if count<10000:
			curcood[0]+=1
			newIm.putpixel(tuple(curcood), im.getpixel((count,0)))
			count+=1
	d-=1
	step=d//2
	for s in range(step):
		if count<10000:
			curcood[1]+=1
			newIm.putpixel(tuple(curcood), im.getpixel((count,0)))
			count+=1
	d-=1
	step=d//2
	for s in range(step):
		if count<10000:
			curcood[0]-=1
			newIm.putpixel(tuple(curcood), im.getpixel((count,0)))
			count+=1
	d-=1
	step=d//2
	for s in range(step):
		if count<10000:
			curcood[1]-=1
			newIm.putpixel(tuple(curcood), im.getpixel((count,0)))
			count+=1
	d-=1
newIm.save("14_rst.jpg")