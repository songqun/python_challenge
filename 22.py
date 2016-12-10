import urllib.request
import io
from PIL import Image, ImageDraw

url = "http://www.pythonchallenge.com/pc/hex/white.gif"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/hex/"
password_mgr.add_password(None, top_level_url, 'butter', 'fly')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data = io.BytesIO(urllib.request.urlopen(url).read())
im = Image.open(data)
newIm=Image.new("RGB", (500,200))
draw=ImageDraw.Draw(newIm)
cx=0
cy=100
for frame in range(im.n_frames):
	im.seek(frame)
	left,up,right,down=im.getbbox()
	dx=left-100
	dy=up-100
	if dx==dy==0:
		cx+=50
		cy=100
	cx+=dx
	cy+=dy
	draw.point([cx,cy])
newIm.show()