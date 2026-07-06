from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")


def levelorder(root):
    if root is None:
        return

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.val, end=" ")

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)


# Example Tree
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder:")
preorder(root)
print()

print("Inorder:")
inorder(root)
print()

print("Postorder:")
postorder(root)
print()

print("Level Order:")
levelorder(root)
print()