# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        res=[]
        q=collections.deque([root])
        while q:
            rightSide=None
            length=len(q)
            for i in range(length):
                node=q.popleft()
                if node:
                    rightSide=node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
# Create nodes
node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node9 = TreeNode(9)
node6 = TreeNode(6)
node10 = TreeNode(10)

# Connect nodes to form the binary tree
node0.left = node1
node0.right = node2
node1.right = node3
node2.left = node4
node4.left = node5
node4.right = node9
node5.left = node6
node5.right = node10

x=Solution()
print(x.rightSideView(node0))