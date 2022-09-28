from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for i in range(len(container) - 1):
        for j in range(len(container) - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]

    return container


my_list = [1, 4, 8, 4, 6, 7, 10, 3]
print(sort(my_list))