from collections import deque

def search_dfs_rec(root, val):
    if root is None or root.value == val:
        return root
    if root.value > val:
        return search_dfs_rec(root.left, val)
    else:
        return search_dfs_rec(root.right, val)

def search_dfs_iter(root, val):
    curr = root
    while curr is not None and curr.value != val:
        if curr.value > val:
            curr = curr.left
        else:
            curr = curr.right
    return curr

def search_bfs(root, val):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.value == val:
            return curr
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return None