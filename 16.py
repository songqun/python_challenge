import urllib.request
import io
from PIL import Image
import numpy as np

url = "http://www.pythonchallenge.com/pc/return/mozart.gif"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/return/"
password_mgr.add_password(None, top_level_url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data = io.BytesIO(urllib.request.urlopen(url).read())
im = Image.open(data)
newIm=Image.new(im.mode,im.size)

for pair in im.getcolors():
	if pair[0]%100==0:
		print(pair)

for j in range(480):
	offset=0
	for i in range(640):
		if im.getpixel((i,j))==195:
			offset=i
			break
	for i in range(640):
		if i>=offset:
			newIm.putpixel((i-offset,j),im.getpixel((i,j)))
		else:
			newIm.putpixel((i+640-offset,j),im.getpixel((i,j)))
newIm.save("16_rst.gif")