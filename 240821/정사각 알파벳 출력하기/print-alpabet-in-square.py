n=int(input())
cnt="A"
for i in range(n):
    for j in range(n):
        print(cnt,end="")
        cnt=chr(ord(cnt)+1)
    print()