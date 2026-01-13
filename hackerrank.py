x = int(input())
y= int(input())
z= int(input())
n= int(input())



l =[]
full_l =[]
for i in range(x+1):
    l=[]
    l.append(i)
    for j in range(y+1):
        l=[i]
        l.append(j)
        # full_l.append(l)
        # l=[i]    
        for k in range(z+1):
            l.append(k)
            if l[0]+l[1]+l[2]!=2:
                full_l.append(l)
            # full_l.append(l)
            l =[i,j]

# full_l.append(l)
print(full_l)


