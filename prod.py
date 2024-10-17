aa=[]
b=[]
n=int(input("Enter no. of elements : "))
for i in range(0,n,1):
      x=int(input("Enter elements : "))
      a.append(x)
print(a)
for j in range(0,n,1):
      y=int(input("Enter elements : "))
      b.append(y)
print(b)
r=0
u=0
for i in range(0,n,1):
      r += a[i]*b[i]
print(r)
