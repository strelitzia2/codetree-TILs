k=int(input())
con=False
for i in range(2,k):
    if k%i==0:
        con=True
        break
if con==True:
    print("C")
else:
    print("P")