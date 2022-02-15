import sys

k,n = map(int,sys.stdin.readline().split())
lines= [int(sys.stdin.readline().strip()) for _ in range(k)]
start, end = 1,sum(lines)//n

while (start<=end) :
  mid = (start+end)//2
  newN = 0
  for line in lines :
    newN+= line//mid
  if newN < n :
    end=mid-1
  else :
    start = mid+1
    
print (end)