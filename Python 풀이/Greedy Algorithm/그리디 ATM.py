N = int(input())

peoples = list(map(int,input().split()))

peoples.sort()

eachTotal = 0
allTotal = 0

for people in peoples :
    eachTotal+=people
    allTotal+=eachTotal

print(allTotal)
