from list.LinkedList import LinkedList


def test_linked_list_add_node() -> None:
    linked_list = LinkedList[int]()
    linked_list.append(1)
    linked_list.append(2)


def test_linked_list_lookup() -> None:
    linked_list = LinkedList[int]()
    linked_list.append(1)
    linked_list.append(2)
    Node = linked_list.lookup(1)
    assert Node is not None
    assert Node.value == 2
    assert linked_list.lookup(2) is None
