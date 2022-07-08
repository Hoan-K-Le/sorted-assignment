li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30,
      1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]


def insertion_sort(li):
    # iterate over the entire list, loop downward when we find a value that is smaller that what is to the left
    for i in range(1, len(li)):
        # we need to know current number for comparison
        # the position sliding back down the list
        j = i
    while (j > 0 and li[j - 1] > li[j]):
        li[j], li[j - 1] = li[j - 1], li[j]
        j -= 1


#  westons way


def insertion_sort(li):
    # iterate over the entire list, loop downward when we find a value that is smaller that what is to the left
    for i in range(1, len(li)):
        # we need to know current number for comparison
        current_number = li[i]
        # the position sliding back down the list
        comparison_position = i - 1
        while comparison_position >= 0 and current_number < li[comparison_position]:
            li[comparison_position], li[comparison_position +
                                        1] = li[comparison_position + 1], li[comparison_position]
            comparison_position -= 1


insertion_sort(li)
print(li)
