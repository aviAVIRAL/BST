

# apne apa kiya  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# AVI :  ye bhai aapne apa kiya by using inoder bst  proprety 
def f(root, arr):
    if not root : return None
    f(root.left, arr)
    arr.append(root.val)
    f(root.right, arr)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = [ ]
        f(root, arr)
        for i in range(len(arr)-1) :
            if arr[i] >= arr[i+1]: return False 
        return True 

        