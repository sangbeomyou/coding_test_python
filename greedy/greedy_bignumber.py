import timeit
start_time = timeit.default_timer() 

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         else:
#             result += data[0]
#             m -= 1
#     if m == 0:
#         break
#     else:
#         result += data[1]
#         m -= 1

count = int(m / (k+1)) * k
count += m % (k + 1)

result += (count) * data[0]
result += (m-count) * data[1]
print(result)
terminate_time = timeit.default_timer() 
print((terminate_time - start_time), "초 걸렸습니다")