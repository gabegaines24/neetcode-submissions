class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            
            # The current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # When going left, the NEW maximum is the current node's value
            # When going right, the NEW minimum is the current node's value
            return validate(node.left, low, node.val) and \
                   validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))