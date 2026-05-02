from search import *
from traversal import *

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if root.value > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def get_height(root):
    if root is None:
        return -1
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return max(left_height, right_height) + 1

if __name__ == '__main__':
    root = None
    values = [10,5,4,12,1,6,8,14,11]
    for val in values:
        root = insert(root, val)

    print("In-order:")
    inorder(root)
    print()

    print("Pre-order:")
    preorder(root)
    print()

    print("Post-order:")
    postorder(root)
    print()

    print(f"Height: {get_height(root)}")

    number = int(input("Enter a value: "))
    find = search_dfs_iter(root, number)
    print(f"Value {number} in a tree: {"Yes" if find else "No"}")
