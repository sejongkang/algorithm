import copy

def solution(a):
    ascending = True
    descending = True
    for i in range(1, 8):
        if a[i] > a[i-1]:
            descending = False
        elif a[i] < a[i-1]:
            ascending = False
    if ascending:
        print('ascending')
    elif descending:
        print('descending')
    else:
        print('mixed')

def solution2(a):
    tmp_desc = copy.deepcopy(a)
    tmp_desc.sort(reverse=True)
    tmp_asc = copy.deepcopy(a)
    tmp_asc.sort()
    if tmp_asc == a:
        print('ascending')
    elif tmp_desc == a:
        print('descending')
    else:
        print('mixed')

a = list(map(int, input().split(' ')))
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# a = [8, 7, 6, 5, 4, 3, 2, 1]
# a = [1, 2, 3, 4, 5, 8, 7, 6]

# solution(a)
solution2(a)
