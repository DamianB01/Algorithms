def merge_sort(arr: list[int], left: int=0, right: int=None) -> None:
    """
    Sort a list using the Merge Sort algorithm with sentinel values.
    The function sorts the input list in ascending order.

    Parameters:
        arr: The list of integers to sort
        left: Starting index of the sublist to sort (default 0)
        right: Ending index of the sublist to sort (default None, which means the last index of the list)

    Time Complexity:
        O(n log n) in all cases
    Space Complexity:
        O(n) due to temporary arrays L and R
    """
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    L = arr[left:mid+1] + [float("inf")]
    R = arr[mid+1:right+1] + [float("inf")]

    i = j = 0
    for k in range(left, right + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
