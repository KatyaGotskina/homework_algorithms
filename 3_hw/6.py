def diameterOfBinaryTree(root) -> int:
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            cur_node, num = stack.pop()

            if cur_node.left == None and cur_node.right == None:
                max_depth = max(max_depth, num)
                continue

            if cur_node.left:
                stack.append((cur_node.left, num + 1))
            
            if cur_node.right:
                stack.append((cur_node.right, num + 1))
        return max_depth