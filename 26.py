import hashlib
data=open('26_mybroken.zip', 'rb').read()
md5='bbb8b499a0eef99b52c7f13f4e78c24b'

for i in range(len(data)):
	for j in range(256):
		newData=data[:i]+bytes([j])+data[(i+1):]
		if hashlib.md5(newData).hexdigest()==md5:
			open('26_rst.zip','wb').write(newData)
			break
