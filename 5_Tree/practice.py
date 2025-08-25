class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root.left == None:
            return 0

        return self.getsum(root)
    
    def getsum(self,node):
        if node == None:
            return 0
        if node.left == None:
            return 0
        
        leftsum = self.getsum(node.left)
        rightsum = self.getsum(node.right)
    
        if node.left.left == None and node.left.right == None:
            return node.left.val + leftsum + rightsum
        else:
            return leftsum + rightsum
        
