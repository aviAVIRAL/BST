




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def build(preorder, bound, index):
    if index[0] == len(preorder) or preorder[index[0]] > bound:
        return None

    root = TreeNode(preorder[index[0]])
    index[0] += 1
    root.left = build(preorder, root.val, index)
    root.right = build(preorder, bound, index)
    return root

class Solution:
    def bstFromPreorder(self, preorder):
        ind = [0]
        return build(preorder, float('inf'), ind )

# Example usage
preorder = [8, 5, 1, 7, 10, 12]
root = Solution().bstFromPreorder(preorder)

# Function to print the BST (inorder traversal for verification)
def inorderTraversal(node):
    if not node:
        return []
    return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

print("Inorder T:", inorderTraversal(root))
print()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(preorder, bound, index):
    # If we've traversed all nodes or the current value exceeds the boundary, return None
    if index == len(preorder) or preorder[index] > bound:
        return None, index

    # Create the root node with the current value
    root = TreeNode(preorder[index])
    index += 1

    # Recursively build the left and right subtrees
    root.left, index = build(preorder, root.val, index)  # Pass updated index
    root.right, index = build(preorder, bound, index)    # Pass updated index
    return root, index

class Solution:
    def bstFromPreorder(self, preorder):
        # Start with index 0
        root, _ = build(preorder, float('inf'), 0)
        return root

# Example usage
preorder = [8, 5, 1, 7, 10, 12]
root = Solution().bstFromPreorder(preorder)

# Function to print the BST (inorder traversal for verification)
def inorderTraversal(node):
    if not node:
        return []
    return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
print("Inorder T:", inorderTraversal(root))

print()