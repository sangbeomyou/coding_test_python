n = int(input())
data = list(map(int, input().split()))
sum = 0
sum_ = 0
data.sort()

for i in range(len(data)):
  sum += sum_ + data[i]
  sum_ += data[i] 

print(sum)