class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder( node, arr):
    if not node:
        return
    inorder(node.left, arr)
    arr.append(node.val)
    inorder(node.right, arr)

def find_kth( root, k):
    arr = []
    inorder(root, arr)
    k_smallest = arr[k - 1]
    k_largest = arr[len(arr) - k]
    return k_smallest, k_largest
# -------------
def print_in_order(root):
    if not root:
        return
    print_in_order(root.left)
    print(root.val, end=" ")
    print_in_order(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print("Binary Search Tree:")
print_in_order(root)
print()

k = 3
print("k:", k)
kth_elements = find_kth(root, k)
print(f" kth samll and kth larg elm are :{kth_elements} ")
