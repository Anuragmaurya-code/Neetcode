# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=True
        def check(root1,root2):
            if (root1==None and root2==None) :
                return 
            elif (root1==None or root2==None) or (root1.val!=root2.val):
                ans=False
                return 
            check(root1.left,root2.left)
            check(root1.right,root2.right)
            return
        check(p,q)
        return ans
x=Solution()
print(x.isSameTree())