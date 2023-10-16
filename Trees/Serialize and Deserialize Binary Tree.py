# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data=""
        queue=collections.deque([root])
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if node:
                    data+=str(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    data+="N"
        
        return data


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        root=TreeNode(int(data[0]))
        queue=collections.deque([root])
        data=data[1:]
        while data!="" or queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if node:
                    if data!="":
                        if data[0]!="N":
                            node.left=TreeNode(int(data[0]))
                            queue.append(node.left)
                        data=data[1:]
                    if data!="":
                        if data[0]!="N":
                            node.right=TreeNode(int(data[0]))
                            queue.append(node.right)
                        data=data[1:]
        return root
        
        
# Create nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Connect nodes to form the binary tree
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(node1))
