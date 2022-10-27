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

    def canReachLeaf(self, root):
        if not root or root.val == 0:
            return False

        if not root.left and not root.right:
            return True
        if BinarySearchTree().canReachLeaf(root.left):
            return True
        if BinarySearchTree().canReachLeaf(root.right):
            return True
        return False

    def leafPath(self, root, path):
        if not root or root.val == 0:
            return False
        path.append(root.val)

        if not root.left and not root.right:
            return True
        if BinarySearchTree().leafPath(root.left, path):
            return True
        if BinarySearchTree().leafPath(root.right, path):
            return True
        path.pop()
        return False


if __name__ == '__main__':
    head = TreeNode(50)
    BinarySearchTree().insert(head, 67)
    BinarySearchTree().insert(head, 43)
    BinarySearchTree().insert(head, 42)
    print(BinarySearchTree().canReachLeaf(head))
