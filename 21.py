import zlib
import bz2

f=open("21_package.pack", "rb")
data=f.read()

rst=""

while True:
    if data.startswith(b'x\x9c'):
        data = zlib.decompress(data)
        rst+=' '
    elif data.startswith(b'BZh'):       
        data = bz2.decompress(data)
        rst+='#'
    elif data.endswith(b'\x9cx'):
        data = data[::-1]
        rst+='\n'
    else:
        break
print(data)
print(rst)