class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    stack = [(root, 1, '')]
    r_max_depth = 0
    l_max_depth = 0

    while stack:
        cur_node, num, side = stack.pop()

        if cur_node.left == None and cur_node.right == None:
            if side == 'r':               
                r_max_depth = max(r_max_depth, num)
            if side == 'l':
                l_max_depth = max(l_max_depth, num)
            continue

        if cur_node.left:
            stack.append(cur_node.left, num + 1, 'l')
        
        if cur_node.right:
            stack.append(cur_node.right, num + 1, 'r')
    return r_max_depth + l_max_depth - 2