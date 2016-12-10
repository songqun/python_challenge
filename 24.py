import urllib.request
import io
from PIL import Image, ImageDraw

url = "http://www.pythonchallenge.com/pc/hex/maze.png"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/hex/"
password_mgr.add_password(None, top_level_url, 'butter', 'fly')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data = io.BytesIO(urllib.request.urlopen(url).read())
im = Image.open(data)
weight,height=im.size

direction=[(0,1), (1,0), (0,-1), (-1,0)]

next_pixel={}

white=(255,255,255,255)
s=(weight-2,0)
t=(1, height-1)
q=[t]
while q:
	v=q.pop(0)
	if v==s:
		break
	for d in direction:
		tmp=(v[0]+d[0], v[1]+d[1])
		if not tmp in next_pixel and 0<=tmp[0]<weight and 0 <=tmp[1]<height and im.getpixel(tmp)!=white:
			next_pixel[tmp]=v
			q.append(tmp)

path=[]
v=s
while v!=t:
	path.append(im.getpixel(v)[0])
	v=next_pixel[v]
open('24_rst.zip','wb').write(bytes(path[1::2]))