a=3127
b=8201
for i in range(2,8201):
    sum=a%i
    num=b%i
    if sum==0 and num==0:
        print (i)