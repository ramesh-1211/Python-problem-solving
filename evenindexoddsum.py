l = list(map(int,input().split()))
odd = l[0:len(l):2]
oddsum = []
for i in odd:
    if i%2!= 0:
        oddsum.append(i)
print(sum(oddsum))
