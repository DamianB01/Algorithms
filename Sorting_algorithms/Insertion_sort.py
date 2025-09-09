def insertion_sort(arr: list[int]) -> None:
    """
    Sort a list using the Insertion Sort algorithm.
    The function sorts the input list in ascending order in place.

    Time Complexity:
        O(n^2) in the worst and average case,
        O(n) in the best case when the list is already sorted.
    Space Complexity:
        O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        