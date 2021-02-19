def solution(log):
    left_stack = []
    right_stack = []
    for char in log:
        if char == '<':
            if left_stack:
                right_stack.insert(0, left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

# def solution2(log):
#     result = []
#     tmp = []
#     while len(log) > 0:
#         char = log.pop(0)
#         if char == '<':
#             if len(result) > 0:
#                 tmp.append(result.pop())
#         elif char == '>':
#             if len(tmp) > 0:
#                 result.append(tmp.pop())
#         elif char == '-':
#             if len(result) > 0:
#                 result.pop()
#         else:
#             result.append(char)
#     while len(tmp) > 0:
#         result.append(tmp.pop())
#     print(''.join(result))

count = int(input())
for _ in range(count):
    log = input()
    solution(log)
    # solution2(log)
