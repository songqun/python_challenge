import pickle
import urllib.request

url="http://www.pythonchallenge.com/pc/def/banner.p"

data=urllib.request.urlopen(url)

text=pickle.load(data)

for i in text:
	print("".join(j[0]*j[1] for j in i))