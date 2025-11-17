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
        




class Solution(object):
    def __init__(self):
        self.result = None
        self.p = 0
        self.q = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q

        self.traversal(root)

        return self.result


    def traversal(self,node):
        if node == None:
            return False
        
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        cur = node.val == self.p or node.val == self.q

        if left and right:
            self.result = node.val
            return False
        if left and cur:
            self.result = node.val
            return False
        if right and cur:
            self.result = node.val
            return False 
        if cur:
            return True

        return False


# S= Solution()
# S.lowestCommonAncestor(TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8))),5,1)


s = "0123456789"
print(s.startswith("0"))

print(s[0:2])

