# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])
        while p_queue and q_queue:
            nodeP = p_queue.popleft()
            nodeQ = q_queue.popleft()

            if not nodeP and not nodeQ:
                continue
            elif not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False

            p_queue.append(nodeP.left)
            p_queue.append(nodeP.right)
            q_queue.append(nodeQ.left)
            q_queue.append(nodeQ.right)

        return True