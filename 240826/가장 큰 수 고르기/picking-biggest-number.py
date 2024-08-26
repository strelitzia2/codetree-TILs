j=input()
arr=j.split()
max=0
for elem in range(len(arr)):
    if elem>max:
        max=elem
print(max)