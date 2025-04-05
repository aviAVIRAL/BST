

# _---------------





# striver repe  

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, target):
        while root  and root.val != target:

 #  rep     root = root.left   if val < root.val   else    root.right

            if target < root.val : 
                root = root.left 
            else: 
                root = root.right
        
        return root

def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val, end=" ")
    printInOrder(root.right)

# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 6
result = solution.searchBST(root, target)

# Displaying the search result
if result is not None:
    print(f"Value {target} found in the BST!")
else:
    print(f"Value {target} not found in the BST.")
                           


print()
#  ---------------
# avi repr e  

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, target):
        while root : 
            if target == root.val : return root
            if target < root.val : 
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


