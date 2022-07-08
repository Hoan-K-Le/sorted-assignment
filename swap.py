swap = [1, 2, 'four', 3]

# swapping easily in python
swap[2], swap[3] = swap[3], swap[2]

print(swap)

li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30,
      1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]
sorted = [0, 1, 2, 3, 4, 5, 6, 7, 9]


# def is_sorted(li):
#     for i in range(len(li) - 1  ):
#         if li[i] > li[i + 1]:
#             li[i], li[i + 1] = li[i + 1], li[i]
#     return True


# def is_sorted(li):
#     sorted = False
#     for array in range(len(li)-1, 0, -1):
#         for i in range(array):
#             if li[i] > li[i + 1]:
#                 sorted = True
#                 li[i], li[i + 1] = li[i + 1], li[i]
#     if not sorted:
#         return

# def is_sorted(li):
#     count = 0
#     for array in range(len(li)-1):
#         if li[array] > li[array + 1]:
#             li[array], li[array + 1] = li[array + 1], li[array]
#             count += 1

#     if count == 0:
#         return li
#     else:
#         return is_sorted(li)


print('it is sorted', is_sorted(li))
# print('unsorted list is', li)
# is_sorted(li)
print('sorted', li)
