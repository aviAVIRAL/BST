












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

print("Inorder Traversal of the BST:", inorderTraversal(root))

# ....................................................

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        def build(preorder, bound):
            nonlocal i
            if i == len(preorder) or preorder[i] > bound:
                return None
            
            root = TreeNode(preorder[i])
            i += 1
            root.left = build(preorder, root.val)
            root.right = build(preorder, bound)
            return root
        
        i = 0
        return build(preorder, float('inf'))

# Example usage
solution = Solution()
preorder = [8, 5, 1, 7, 10, 12]
root = solution.bstFromPreorder(preorder)

# Function to print the BST (inorder traversal for verification)
def inorderTraversal(node):
    if not node:
        return []
    return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

print("Inorder Traversal of the BST:", inorderTraversal(root))
