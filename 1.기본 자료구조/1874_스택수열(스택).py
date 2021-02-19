def solution(n):
    count = 1
    stack = []
    result = []

    for i in range(1, n + 1):
        data = int(input())
        while count <= data:
            stack.append(count)
            count += 1
            result.append('+')
        if stack[-1] == data:
            stack.pop()
            result.append('-1')
        else:
            print('NO')
            exit(0)
    print('\n'.join(result))


def solution2(list, count):
    stack = []
    result = []
    mark = []
    index = 0
    for i in range(1, count + 1):
        stack.append(i)
        mark.append('+')
        while len(stack) != 0 and stack[-1] == list[index]:
            result.append(stack.pop())
            mark.append('-')
            index += 1
            if index == count:
                break
        i += 1

    if result != list:
        print('NO')
    else:
        for i in mark:
            print(i)

# 1번 방식
n = int(input())
solution(n)


# 2번 방식
count = int(input())
list = []

for i in range(count):
    list.append(int(input()))

solution2(list, count)

