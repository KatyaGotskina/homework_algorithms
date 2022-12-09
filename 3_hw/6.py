# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    if not root: 
        return 0
    d = {None: -1}
    q = [root]
    ans = 0
    while q:
        node = q[-1]
        if node.left in d and node.right in d:
            q.pop()
            l = d[node.left] + 1
            r = d[node.right] + 1
            ans = max(ans, l + r)
            d[node] = max(l, r)
        else:
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
    return ans
