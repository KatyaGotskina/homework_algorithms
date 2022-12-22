# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def trimBST(self, root, L, R):

        if not root:
            return None

        left = self.trimBST(root.left, L, R)
        right = self.trimBST(root.right, L, R)

        if root.val >= L and root.val <= R:
            root.left = left
            root.right = right
        else:
            if left:
                root = left
            else:
                root = right
        return root

