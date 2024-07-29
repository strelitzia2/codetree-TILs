e=int(input())
count=0
while True:
    if e==1:
        break
    elif e%2==0:
        e=e//2
        count+=1
    else:
        e=e*3+1
        count+=1
print(count)