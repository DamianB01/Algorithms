def counting_sort(arr: list[int], val: int=None) -> list[int]:
    """
    Sort a list of non-negative integers using the Counting Sort algorithm.
    The function returns a new sorted list in ascending order.

    Parameters:
        arr: List of non-negative integers to sort
        val: Maximum value in arr (optional). If None, the function computes max(arr)

    Time Complexity:
        O(n + k) where n = len(arr) and k = maximum value in arr

    Space Complexity:
        O(n + k) due to the output array `res` and the helper array `freq`

    Returns:
        A new sorted list containing the elements of `arr`
     """
    if val is None:
        val = max(arr)

    res = [0] * len(arr)
    freq = [0] * (val + 1)

    for i in range(len(arr)):
        freq[arr[i]] += 1

    for i in range(1, val + 1):
        freq[i] += freq[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        res[freq[arr[i]] - 1] = arr[i]
        freq[arr[i]] -= 1

    return res
