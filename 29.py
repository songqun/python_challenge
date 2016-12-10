import urllib.request
import io
import bz2

url="http://www.pythonchallenge.com/pc/ring/guido.html"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/ring/"
password_mgr.add_password(None, top_level_url, 'repeat', 'switch')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
line=data.splitlines()[12:]
data=bytes([len(i) for i in line])
print(bz2.decompress(data))