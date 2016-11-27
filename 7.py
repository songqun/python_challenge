import urllib.request
import io
from PIL import Image

url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
data = io.BytesIO(urllib.request.urlopen(url).read())
im = Image.open(data)
rgb=[]
for i in range(0,608,7):
	rgb.append(im.getpixel((i,47))[0])
word=[]
for i in range(len(rgb)):
	word.append(chr(rgb[i]))
print("".join(word))
ans=[]
key=[105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in range(len(key)):
	ans.append(chr(key[i]))
print("".join(ans))
	