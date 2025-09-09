import random

def quick_sort(arr: list[int], left: int, right: int) -> None:
    """
        Sort a list using the Quick Sort algorithm.
        The function sorts the input list in ascending order in place.

        Parameters:
            arr: The list of integers to sort
            left: Starting index of the sublist to sort
            right: Ending index of the sublist to sort

        Time Complexity:
            O(n log n) in average and the best cases
            O(n^2) in the worst case (very unlikely due to random pivot)
        Space Complexity:
            O(log n)
    """
    if left < right:
        pivot_ind = random.randint(left, right)
        arr[pivot_ind], arr[right] = arr[right], arr[pivot_ind]
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)

def partition(arr: list[int], left: int, right: int) -> int:
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i
