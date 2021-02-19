def solution(queue):
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

def solution2(list, index):
    chk = [0 for index in range(len(list))]
    chk[index] = 1
    num = 1
    while len(list) != 0:
        if list[0] == max(list):
            list.pop(0)
            if chk.pop(0) == 1:
                return str(num)
            num += 1
        else:
            list.append(list.pop(0))
            chk.append(chk.pop(0))

# 솔루션1 사용시
test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))

    solution(queue)

# 솔루션2 사용시
result = []
for i in range(int(input())):
    case, index = map(int, input().split(' '))
    lists = list(map(int, input().split(' ')))

    result.append(solution2(lists, index))

print('\n'.join(result))

