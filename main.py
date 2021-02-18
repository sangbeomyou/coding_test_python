# m =3 
# n =4
# a = [m * [0] for _ in range(n)]
# print(a)
# a[1][1] = 4
# print(a)
# data = dict()
# data['사과'] = 'apple'
# data['바나나'] = 'banana'
# print(data)
# key = list(data.keys())
# value = data.values()
# print(key)
# print(value)
# for i in key:
#   print(data[i])
# data = [1,1,2,3,3,4,5,5]
# a= set(data)
# # print(a)
# a = int(input())
# data = list(map(int, input().split()))
# print(a)
# print(data)
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#   data = list(map(int, input().split()))
#   min_data = min(data)
#   result = max(result, min_data)
# # print(result)
# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# # 1부터 10까지의 무게를 담을 수 있는 리스트
# array = [0] * 11

# for x in data:
#     # 각 무게에 해당하는 볼링공의 개수 카운트
#     array[x] += 1

# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m + 1):
#     n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     print(n)
#     result += array[i] * n # B가 선택하는 경우의 수와 곱해주기
#     print(result)
# print(result)

for i in range(18):
  print(i % 3)