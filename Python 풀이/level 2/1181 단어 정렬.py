import sys

N = int(input())
words = []

for i in range (N):
  words.append(sys.stdin.readline().strip()) # strip으로 \n 제거

setwords = set(words) # set을 통해 중복 제거
newWords = list(setwords)

newWords.sort()
newWords.sort(key = len)

for word in newords :
  print(word)