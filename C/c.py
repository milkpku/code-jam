import math as c
filename = 'C-large.in'
outfile = 'c.out'
outhandle = open(outfile,'w')
fhandle = open(filename,'r')
s = fhandle.read()
s = s.split('\n')

def if_p(x):
	
# print s

# get the test number
n = int(s[0])

for i in range(n):

	key = s[i*2+1]
	target = int(s[i*2+2])

	print key, target
	# record line
	record = [-1]*(target+10)

	key = key.split(' ')
	# print key
	print key
	for j in range(10):
		if key[j] == '1':
			record[j] = 1;

	for j in range(4, target+1):

		# if j can be get directly
		num = j
		count = 1
		while num > 0:
			if record[num%10] != 1:
				count = 0
				break
			num = num / 10
		if count == 1:
			if record[j] == -1:
				record[j] = len(str(j))

		# if can derived by multipy 

		for k in range(1,int(c.sqrt(j))+1):
			if j%k ==0:

				if (record[k]!=-1)&(record[j/k]!=-1):
					if (record[j] == -1)or(record[k]+record[j/k] + 1<record[j]):
						record[j] = record[k]+record[j/k] + 1


	if record[target]>0:
		outhandle.write('Case #'+str(i+1)+': '+str(record[target]+1)+'\n')
	else:
		outhandle.write('Case #'+str(i+1)+': Impossible\n')

fhandle.close()
outhandle.close

