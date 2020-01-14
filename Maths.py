import csv 
import random
import math

file = open("found.txt",'r')
l=file.readlines()
n=int(len(l)*80/100)
x=[]
for i in range(0,len(l)):
    x.append(i)
random.shuffle(x)
train=x[0:n+1]
test=x[n+1:]

sx=0
sy=0
sx2=0
sy2=0
sxy=0
count=0
for r in l:
    count+=1        
    if count in train:
        p=r.find(';')
        q=r.find(';',p+1)
        k=float(r[p+1:q])
        l=float(r[q+1:])
        sx+=k
        sy+=l
        sx2+=k*k
        sy2+=l*l
        sxy+=k*l

a=((sxy/n)-(sx*sy/(n*n)))/(sx2/n - sx*sx/(n*n))
b=sy/n - a*sx/n
r=((sxy/n)-(sx*sy/(n*n)))/math.sqrt((sx2/n - sx*sx/(n*n))*(sy2/n - sy*sy/(n*n)))
print("Correlation Coefficient:",r)
print("Rgression line is: y =",a,"x +",b)

file = open("found.txt", 'r')
l=file.readlines()
count=0
e=0
for r in l:
    count+=1
    if count in test:
        p=r.find(';')
        q=r.find(';',p+1)
        k=float(r[p+1:q])
        l=float(r[q+1:])
        temp=l-(a*k+b)
        e+=temp*temp
print("Mean Square Error is:",e/125)

cl=[]
hl=[]
il=[]
filename='conferences.csv'
with open(filename, 'r') as csvfile:
    c = csv.reader(csvfile)
    count=0
    k=l=0
    for r in c:
        for i in range(1,len(r)):
            r[0]+=r[i]
        k=r[0].find('"')
        l=r[0].find('"',k+1)
        conf=r[0][k+1:l]
        cl.append(conf)
        m=-1
        for i in range(7):
            m=r[0].find(';',m+1)
        n=r[0].find(';',m+1)
        hi=r[0][m+1:n]
        try:
            hi=int(hi)
        except:
            hi=-1
        hl.append(hi)
        if hi!=-1:
            impf=a*hi+b
        else:
            impf='Not able to find impact factor because of asymmetric data'
        il.append(impf)

file = open('conferences if.txt', 'w')
for i in range(1,len(cl)):
    file.write(cl[i]+";"+str(hl[i])+";"+str(il[i])+'\n')
