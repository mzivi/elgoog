class Node:
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def bst(key_value_pairs):
    root = None
    for k, v in key_value_pairs.items():
        if not root:
            root = Node(k, v)
        else:
            bst_insert(root, k, v)
    return root


def bst_insert(root, key, value):
    if key <= root.key:
        if root.left:
            bst_insert(root.left, key, value)
        else:
            root.left = Node(key, value, root)
    else:  # key > root.key
        if root.right:
            bst_insert(root.right, key, value)
        else:
            root.right = Node(key, value, root)


def bst_find(root, key):
    result = None
    while root:
        if key == root.key:
            result = root
            break
        root = root.left if key < root.key else root.right
    return result


def bst_remove(root, key):
    node = bst_find(root, key)
    if not node:
        return None

    if node.left and node.right:
        _bst_remove_internal(node)
    else:
        if not node.left:
            new_node = node.right
        else:  # node.right == None
            new_node = node.left
        if node.parent:
            if node.parent.left == node:
                node.parent.left = new_node
            else:
                node.parent.right = new_node
    return node.key, node.value


def _bst_remove_internal(node):
    new_node = _bst_leftmost(node.right)
    new_node.parent = node.parent
    new_node.left = node.left
    new_node.right = node.right
    if node.parent:
        if node.parent.left == node:
            node.parent.left = new_node
        else:
            node.parent.right = new_node


def _bst_leftmost(node):
    return None


def bst_traverse(root, fun):
    if not root:
        return

    if root.left:
        bst_traverse(root.left, fun)
    fun(root.key, root.value)
    if root.right:
        bst_traverse(root.right, fun)


if __name__ == '__main__':
    root = bst({n: n * n for n in [5, 2, 3, 7, 4]})
    bst_traverse(root, lambda k, v: print('{}: {}'.format(k, v)))
    print(bst_find(root, 3).value)
