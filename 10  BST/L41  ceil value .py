

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findCeil(self, root, key):
        ceil = -1
        while root:
            if root.val == key:
                ceil = root.val
                return ceil
            if key > root.val:
                root = root.right
            else: #  root.value  > then key se 
                ceil = root.val
                root = root.left
        return ceil

def printInOrder(root):
    # Check if the current node
    # is null (base case for recursion)
    if not root:
        # If null, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)
    
    # Print the value of the current node
    print(root.val, end=" ")
    
    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

# Creating a BST
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
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 8
ciel = solution.findCeil(root, target)

if ciel != -1:
    print(f"Ceiling of {target} is: {ciel}")
else:
    print("No ceiling found!")
                           
                        
