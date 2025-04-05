
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        while root : 
            if val == root.val : return root
            if val < root.val : 
                root = root.left 
            else: 
                root = root.right
        return None

# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

# print("Binary Search Tree:")
# printInOrder(root)
# print()

solution = Solution()

# Searching for a value in the BST
target = 8
root = solution.searchBST(root, target)


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val, end=" ")
    printInOrder(root.right)

root = printInOrder(root)

# Displaying the search result
# if result is not None:
#     print(f"Value {target} found in the BST!")
# else:
#     print(f"Value {target} not found in the BST.")
                           
                        







