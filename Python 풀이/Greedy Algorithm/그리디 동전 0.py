N , K = map(int,input().split()) # N=10, K=4200
count = 0
list = []
for i in range (N) :
  list.append(int(input()))
  
list.sort(reverse=True)

for price in list :
  if price<=K :
    count+=K//price
    K%=price

print(count)