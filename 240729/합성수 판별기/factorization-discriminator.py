k=int(input())
c=False
for i in range(2,k):
    if k%i==0:
        c=True
        break
if c==True:
    print("C")
else:
    print("N")