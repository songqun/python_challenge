import urllib.request
import io
from PIL import Image

url="http://www.pythonchallenge.com/pc/rock/mandelbrot.gif"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/rock/"
password_mgr.add_password(None, top_level_url, 'kohsamui', 'thailand')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data=io.BytesIO(urllib.request.urlopen(url).read())

im=Image.open(data)
left=0.34
top=0.57
width=0.036
height=0.027
iterations=128

w,h=im.size
xstep=width/w
ystep=height/h

rst=[]

for y in range(h-1, -1, -1):
	for x in range(w):
		c=complex(left+x*xstep, top+y*ystep)
		z=0+0j
		for i in range(iterations):
			z=z*z+c
			if abs(z)>2:
				break
		rst.append(i)
im2=im.copy()
im2.putdata(rst)
diff=[(a-b) for a,b in zip(im.getdata(), im2.getdata()) if a!=b]
print([i for i in range(2,len(diff)) if len(diff)%i==0])

plot=Image.new('L', (23,73))
plot.putdata([(i<16) and 255 or 0 for i in diff])
plot.resize((230,730)).save('31_rst.png')