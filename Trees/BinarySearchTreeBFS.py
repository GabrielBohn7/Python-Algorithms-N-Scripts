from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def search(self, root, target):
        if not root:
            return False

        if target > root.val:
            return BinarySearchTree().search(root.right, target)
        elif target < root.val:
            return BinarySearchTree().search(root.left, target)
        else:
            return True

    # Insert a new node and return the root of the BST.
    def insert(self, root, val):
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = BinarySearchTree().insert(root.right, val)
        elif val < root.val:
            root.left = BinarySearchTree().insert(root.left, val)
        return root

    # Return the minimum value node of the BST.
    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    # Remove a node and return the root of the BST.
    def remove(self, root, val):
        if not root:
            return None

        if val > root.val:
            root.right = BinarySearchTree().remove(root.right, val)
        elif val < root.val:
            root.left = BinarySearchTree().remove(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = BinarySearchTree().minValueNode(root.right)
                root.val = minNode.val
                root.right = BinarySearchTree().remove(root.right, minNode.val)
        return root

    def printTree(self, node, level=0):
        if node != None:
            BinarySearchTree().printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            BinarySearchTree().printTree(node.right, level + 1)

    def bfs(self, root):
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            print("level: ", level)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

if __name__ == '__main__':
    head = TreeNode(50)
    BinarySearchTree().insert(head, 67)
    BinarySearchTree().insert(head, 43)
    BinarySearchTree().bfs(head)
