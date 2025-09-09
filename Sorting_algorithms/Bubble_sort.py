def bubble_sort(arr: list[int]) -> None:
    """
    Sort a list using the Bubble Sort algorithm.
    The function sorts the input list in ascending order in place.

    Time Complexity:
        O(n^2) in the worst and average case,
        O(n) in the best case when the list is already sorted.
    Space Complexity:
        O(1)
    """
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break