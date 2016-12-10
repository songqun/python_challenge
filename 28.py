import urllib.request
import io
from PIL import Image

url="http://www.pythonchallenge.com/pc/ring/bell.png"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/ring/"
password_mgr.add_password(None, top_level_url, 'repeat', 'switch')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data=io.BytesIO(urllib.request.urlopen(url).read())
im=Image.open(data)
g=list(im.split()[1].getdata())
diff=[abs(a-b) for a,b in zip(g[0::2], g[1::2])]
#print(diff)
filte=list(filter(lambda x: x!=42, diff))
print(bytes(filte).decode())