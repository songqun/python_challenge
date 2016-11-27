import urllib.request
import io


url = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "http://www.pythonchallenge.com/pc/return/"
password_mgr.add_password(None, top_level_url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
data = io.BytesIO(urllib.request.urlopen(url).read()).read()

for i in range(5):
	open('12_%d_rst.jpg'%i, 'wb').write(data[i::5])