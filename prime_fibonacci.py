import math
def checkPrime(n):
	if n==1:
		return False
	i=2
	while i*i<=n:
		if n%i==0:
			return False
		i+=1
	return True

def merge(qwe):
    asd=[]
    for i in range(len(qwe)):
        for j in range(len(qwe)):
            if i!=j:
                x=int(qwe[i]+qwe[j])
                if(checkPrime(x)) and x not in asd:
                    asd.append(x)
    return asd


a,b=input().split()
a=int(a)
b=int(b)

prime=[]
i=a
while i<b:
	if(checkPrime(i)):
		prime.append(str(i))
	i+=1


merged=merge(prime)
mx=max(merged)
mn=min(merged)
num=len(merged)

ans=0

for i in range(1,num-1):
	ans=mn+mx
	mn=mx
	mx=ans

print(ans)