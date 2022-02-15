import sys

k,n = map(int,sys.stdin.readline().split())

lines = [int(sys.stdin.readline()) for _ in range(k)]

start,end = 1,max(lines)

while (start>=end) :
  mid = (start+end)//2
  sum=0
  for line in lines:
      sum+=line//mid
  
  if sum < n :
    end=mid-1
  else :
    start=mid+1
    
print(end)
    
