from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(elem, arr)
    count = 0

    left = 0
    right = len(arr) - 1
    while left < right:
        count += 1
        mid = (left + right) // 2
        if arr[mid] == elem:
            print(elem, count)
            return mid
        elif arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
    if arr[left] == elem:
        print(elem, count)
        return left
    print("None", count)
    return None


if __name__ == "__main__":
    a = list(range(100))
    binary_search(49, a)
