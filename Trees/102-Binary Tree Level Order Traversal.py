from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        queue=deque([root])
        ans=[]
        while(queue):
            temp=[]
            for i in range(len(queue)):
                node=queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

# Connect nodes to form the binary tree
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

x=Solution()
print(x.levelOrder(node3))