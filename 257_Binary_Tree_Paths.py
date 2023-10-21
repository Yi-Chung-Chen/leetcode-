# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root, p=''):
            path = p
            path+=str(root.val)
            if not root.left and not root.right:
                ans.append(path)
                return
            if root.left:
                dfs(root.left, path+'->')
            if root.right:
                dfs(root.right, path+'->')
        dfs(root)
        # 這題沒啥好講，就用dfs幹下去就對了，不過要設定一個邏輯是左右都要沒有根結點時，才可以把字串新增到ans內
        return ans
