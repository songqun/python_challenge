import urllib.request
import io
from PIL import Image

url="http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/ring/"
password_mgr.add_password(None, top_level_url, 'repeat', 'switch')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode()
data_str=[i.strip() for i in data.split(',')]

length=len(data_str)
factor=[i for i in range(2, length) if length%i==0]
print(factor)
im=Image.new("F",(53,139))
im.putdata([float(i) for i in data_str], 256)
im=im.transpose(Image.FLIP_LEFT_RIGHT)
im=im.transpose(Image.ROTATE_90)
#im.show()

x=data_str[0::3]
y=data_str[1::3]
z=data_str[2::3]

print(bytes([int(i[0][5]+i[1][5]+i[2][6]) for i in zip(x,y,z)]))