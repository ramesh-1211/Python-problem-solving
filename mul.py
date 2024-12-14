n,m= map(int,input().split())
if n<m:
    print(1)
elif n%m==0:
    print(n//m)
else:
    print(n//m+1) 