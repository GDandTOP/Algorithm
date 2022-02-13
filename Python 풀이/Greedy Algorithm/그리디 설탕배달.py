n = int(input("입력해라 : "))
#18
num=0
while(n>0):
    if (n%5==0):
        num+=n//5
        n%=5
    else:
        n-=3
        num+=1

if (n==0):
    print(num)
else:
    print(-1)