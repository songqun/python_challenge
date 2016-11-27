num="1"
for loop in range(30):
	line=[]
	count=1
	for i in range(0,len(num)-1):
		if num[i]==num[i+1]:
			count+=1;
		else:
			line.append(str(count))
			line.append(num[i])
			count=1
	line.append(str(count))
	line.append(num[len(num)-1])
	num="".join(line)
print(len(num))