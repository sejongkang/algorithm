array = input()
list = []
for i in array:
    list.append(int(i))
list.sort(reverse=True)
for item in list:
    print(item, end='')
#
# for i in range(9, 1,  -1):
#     for j in array:
#         if int(j) == i:
#             print(i, end='')