import urllib.request
import io
import wave
from PIL import Image

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/hex/"
password_mgr.add_password(None, top_level_url, 'butter', 'fly')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
data=[0 for i in range(25)]

for i in range(25):
	url=top_level_url+"lake"+str(i+1)+".wav"
	opener.open(url)
	urllib.request.install_opener(opener)
	data[i] = io.BytesIO(urllib.request.urlopen(url).read())

waves=[wave.open(data[i]) for i in range(25)]
rst=Image.new('RGB', (300, 300), 0)
frameNum=waves[0].getnframes()
for i in range(len(waves)):
	byte=waves[i].readframes(frameNum)
	im=Image.frombytes('RGB', (60,60), byte)
	rst.paste(im, (60*(i%5), 60*(i//5)))
rst.save('25_rst.png')