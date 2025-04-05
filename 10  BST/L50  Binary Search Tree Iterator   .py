# class BSTIterator:

#     def __init__( root: Optional[TreeNode]):
#         stack = []
#         pushAllLeft(root)

#     def next(self) -> int:
#         if stack:
#             value = stack.pop()
#             pushAllLeft(value.right)
#             return value.val
        
#     def hasNext(self) -> bool:
#         if not stack:
#             return False
#         return True 
    
#     def pushAllLeft(node):
#         while node:
#             stack.append(node)
#             node=node.left
