import csv
jcl=[]
hl=[]

with open("journals.csv",'r') as csvfile:
    c = csv.reader(csvfile)
    for r in c:
        for i in range(1,len(r)):
            r[0]+=r[i]
        k=r[0].find('"')
        l=r[0].find('"',k+1)
        jour=r[0][k+1:l]
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
        jcl.append(jour)
jcl=jcl[1:]
hl=hl[1:] 

jtl=[]
il=[]
file = open('journals.txt','r')
l=file.readlines()
for r in l:
    j=r.find(';')
    k=r.find(';',j+1)
    jtl.append(r[j+1:k])
    il.append(r[k+1:])

file = open("found.txt",'w')
for i in range(len(jcl)):
    for j in range(len(jtl)):
        if jcl[i].lower()==jtl[j].lower():
            file.write(jcl[i]+";"+str(hl[i])+";"+str(il[j]))
            break

            
    
    
    
    
    
    
    

    
    
