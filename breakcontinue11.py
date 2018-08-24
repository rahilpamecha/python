for n in range(10):
    if n==6:
        break
    print(n,end=',')

for n in range(10):
    if n%2 ==0:
        print("even",n)
        continue
    print("old",n)

for i in range(10):
    print(i,"\"free\"")