import urllib.request
import io
from PIL import Image
import bz2
import keyword

url="http://www.pythonchallenge.com/pc/hex/zigzag.gif"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/hex/"
password_mgr.add_password(None, top_level_url, 'butter', 'fly')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data=io.BytesIO(urllib.request.urlopen(url).read())
im=Image.open(data)

palette=im.getpalette()[::3]
table=bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))
imData=im.tobytes()
imNewData=imData.translate(table)
diff=list(filter(lambda d: d[0] != d[1], list(zip(imData[1:],imNewData[:-1]))))

string=[p[0] for p in diff]
text=bz2.decompress(bytes(string))

print(set([word for word in text.split() if not keyword.iskeyword(word.decode())]))