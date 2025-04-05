




                            
# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def floorInBST(self, root, key):
        floor = -1
        while root:
           
            if root.val == key:
                floor = root.val
                return floor
            
            if key > root.val:
             
                floor = root.val
                root = root.right
            else:
                root = root.left
        
        return floor

def printInOrder(root):
    # Check if the current node
    # is null (base case for recursion)
    if root is None:
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
ciel = solution.floorInBST(root, target)

if ciel != -1:
    print(f"Floor of {target} is: {ciel}")
else:
    print("No floor found!")
                           
                        