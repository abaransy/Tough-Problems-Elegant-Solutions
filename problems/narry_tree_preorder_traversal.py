# recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        pre_order = []

        self.helper(root, pre_order)

        return pre_order

    def helper(self, root, pre_order) -> None:
        if root:
            pre_order.append(root.val)

            for child in root.children:
                self.helper(child, pre_order)

# iterative

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
          return []

        stack = [root]
        pre_order = []

        while stack:
            root = stack.pop()
            pre_order.append(root.val)
            stack.extend(root.children[::-1])

        return pre_order