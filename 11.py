import urllib.request
import io
from PIL import Image

url = "http://www.pythonchallenge.com/pc/return/cave.jpg"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/return/"
password_mgr.add_password(None, top_level_url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data = io.BytesIO(urllib.request.urlopen(url).read())
im = Image.open(data)

odd=Image.new(im.mode, (320,240))
even=Image.new(im.mode, (320,240))
for j in range(480):
	for i in range(640):
		if i%2==0 and j%2==0:
			even.putpixel((int(i/2),int(j/2)),im.getpixel((i,j)))
		elif i%2==1 and j%2==1:
			odd.putpixel((int((i-1)/2), int((j-1)/2)),im.getpixel((i,j)))
even.save("11_even.jpg")
odd.save("11_odd.jpg")