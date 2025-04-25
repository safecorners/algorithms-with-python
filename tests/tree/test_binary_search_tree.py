from tree.binary_search_tree import BinarySearchTree


def test_bst_initialization() -> None:
    bst = BinarySearchTree[int]()
    assert bst.root is None


def test_bst_insert() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(10)


def test_bst_insert_left() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)

    assert bst.root is not None
    assert bst.root.value == 10

    assert bst.root.left is not None
    assert bst.root.left.value == 5


def test_bst_insert_right() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(15)

    assert bst.root is not None
    assert bst.root.value == 10

    assert bst.root.right is not None
    assert bst.root.right.value == 15


def test_bst_insert_multiple() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(14)
    bst.insert(6)
    bst.insert(17)
    bst.insert(1)
    bst.insert(7)
    bst.insert(21)

    node = bst.search(1)

    assert node is not None
    assert node.parent is not None
    assert node.parent.value == 6
    assert node.parent.parent is not None
    assert node.parent.parent.value == 14


def test_remove_node_with_no_children() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    node = bst.search(5)
    assert node is not None
    bst.remove(node)

    assert bst.root is not None
    assert bst.root.left is None


def test_remove_node_with_one_child() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)

    node = bst.search(5)
    assert node is not None
    bst.remove(node)

    assert bst.root is not None
    assert bst.root.left is not None
    assert bst.root.left.value == 3


def test_remove_node_with_two_children() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(67)

    bst.insert(60)
    bst.insert(81)

    bst.insert(59)
    bst.insert(63)
    bst.insert(58)

    bst.insert(78)
    bst.insert(92)

    bst.insert(91)
    bst.insert(95)

    node = bst.search(81)
    assert node is not None
    parent = node.parent

    bst.remove(node)

    assert parent is not None
    assert parent.value == 67
    assert parent.right is not None
    assert parent.right.value == 91

    prev_parent = bst.search(92)
    assert prev_parent is not None
    assert prev_parent.left is None
