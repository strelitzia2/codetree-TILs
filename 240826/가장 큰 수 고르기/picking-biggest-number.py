j=input()
arr=j.split()
maxl=0
for elem in range(arr):
    if elem>maxl:
        maxl=elem
print(maxl)