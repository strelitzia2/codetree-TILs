arr = list(map(int, input().split()))
maxl=0
for elem in arr:
    if elem>maxl:
        maxl=elem
print(maxl)