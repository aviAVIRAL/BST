

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(preorder, bound, index):
    if index == len(preorder) or preorder[index] > bound:
        return None

    root = TreeNode(preorder[index])
    index += 1
    root.left = build(preorder, root.val, index)
    root.right = build(preorder, bound, index)
    return root

class Solution:
    def bstFromPreorder(self, preorder):
        
        return build(preorder, float('inf'), 0 )

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