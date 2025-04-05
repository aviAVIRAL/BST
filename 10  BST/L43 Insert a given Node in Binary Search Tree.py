


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
    def insertIntoBST(self, root, Target):
        # If the tree is empty, create a new node and return it
        if root is None:
            return TreeNode(Target)

        cur = root

        while True:
            # If the value to insert is greater than the current node's value
            if Target > cur.val:
                # Move to the right subtree if it exists
                if cur.right is not None:
                    cur = cur.right
                else:
                    # Otherwise, insert the new node here
                    cur.right = TreeNode(Target)
                    break
            else:  # The value to insert is less than or equal to the current node's value
                # Move to the left subtree if it exists
                if cur.left is not None:
                    cur = cur.left
                else:
                    # Otherwise, insert the new node here
                    cur.left = TreeNode(Target)
                    break

        return root


# Function to print the tree in InOrder traversal
def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val, end=" ")
    printInOrder(root.right)


# Example usage
solution = Solution()

# Creating a BST
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)  # Fixed tree structure

target = 5
root = solution.insertIntoBST(root, target)  # Corrected instantiation

print("Binary Search Tree after insertion:")
printInOrder(root)
print()

