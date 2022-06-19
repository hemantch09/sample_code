l= [1, 5, 10, 110, 80]
ln=[]
i= 0
counter=-1
while i<len(l):
    j=l[i]
    for k in l:
        if l.index(j)==l.index(k):
            continue
        else:
            n= j + k
            if n in l:
                ln.append([n,j,k])
    i+=1
if len(ln)!=0:
    print(ln)
else:
    print("sorry no triplets")
