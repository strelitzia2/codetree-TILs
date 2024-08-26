j=input()
arr=j.split()
maxl=0
for elem in range(len(arr)):
    if elem>maxl:
        maxl=elem
print(maxl)