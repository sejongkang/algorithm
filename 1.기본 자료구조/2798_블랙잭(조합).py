from itertools import combinations

def solution(data,m):
    # 가장 큰 합
    result = 0
    length = len(data)

    count = 0
    for i in range(0, length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                sum_value = data[i] + data[j] + data[k]
                if sum_value <= m:
                    # 합을 비교하여 큰 값으로 갱신
                    result = max(result, sum_value)
    print(result)

def solution2(a):
    b = list(combinations(a, 3))
    results = []
    for item in b:
        if sum(item)<= val:
            results.append(sum(item))
    print(max(results))

count, val = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))

solution(a,val)
solution2(a)
# a = [5, 6, 7, 8, 9]