n = int(input())
data=[]

for i in range(n):
  data.append(int(input()))

data.sort(reverse=True)
sum = 0
for i in range(n):
  if i % 3 != 2:
    sum += data[i]
print(sum)