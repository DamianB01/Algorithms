def selection_sort(arr: list[int]) -> None:
    """
    Sort a list using the Selection Sort algorithm.
    The function sorts the input list in ascending order in place.

    Time Complexity:
        O(n^2) in all cases
    Space Complexity:
        O(1)
    """
    for i in range(len(arr) - 1):
        temp = i
        for j in range(i + 1, len(arr)):
            if arr[temp] > arr[j]:
                temp = j
        arr[temp], arr[i] = arr[i], arr[temp]
