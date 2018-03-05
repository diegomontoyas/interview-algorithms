# https://www.interviewbit.com/courses/programming/topics/trees/problems/max-depth-of-binary-tree/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if not A: return 0
        return 1 + max(self.maxDepth(A.left), self.maxDepth(A.right))

