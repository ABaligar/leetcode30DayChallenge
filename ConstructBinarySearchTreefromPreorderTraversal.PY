#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def formBST(remaining_list, left=True, left_limit=0, right_limit=pow(10,8)):
            if not remaining_list:
                return None
            element = remaining_list[0]
            if element> left_limit and element < right_limit:
                node = TreeNode(element)
                remaining_list.pop(0)  ## place of pop important
                node.left = formBST(remaining_list, True, left_limit, element)
                node.right = formBST(remaining_list, False, element, right_limit)
                return node
            else:
                return None
        
        return formBST(preorder, True)    
    
        

    
        
        
