n,c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

# 최소로 떨어질 수 있는 거리
start = array[1] - array[0]
# 최대로 떨어질 수 있는 거리
end = array[-1] - array[0]

result = 0

while(start<=end):
    # 떨어진 거리 = 최소와 최대의 중간 거리
    mid = (start+end)//2
    # 거리 계산 기준 집 = 첫 집
    value = array[0]
    # 첫집에 설치한 1개
    count = 1
    # 마지막 집까지 탐색
    for i in range(1, len(array)):
        # 탐색한 집의 거리가 기준 집 + 떨어진 거리보다 크면
        if array[i] >= value + mid:
            count += 1
            value = array[i]
    # 떨어진 거리가 좁아서 원하는 개수보다 크면
    if count >= c:
        # 해당 거리를 최소값으로 변경
        start = mid + 1
        # 설치는 가능하니 해당 거리를 결과로 저장
        result = mid
    # 해당 거리가 멀어서 원하는 수보다 적으면
    else:
        # 해당 거리를 최대값으로 변경
        end = mid - 1

print(result)