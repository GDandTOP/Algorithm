import sys

while(1) :
  N = int(sys.stdin.readline().strip())
  if N==0 :
    break
  if int(str(N)[::-1])==N : # 문자열로 전환후 reverse 동작
    print("yes")
  else :
    print("no")
    