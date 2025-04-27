from stack.linked_list_stack import LinkedListStack


def test_push_and_pop() -> None:
    stack = LinkedListStack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.size() == 0


def test_peek() -> None:
    stack = LinkedListStack[str]()
    assert stack.peek() is None
    stack.push("a")
    assert stack.peek() == "a"
    stack.push("b")
    assert stack.peek() == "b"
    stack.pop()
    assert stack.peek() == "a"


def test_is_empty() -> None:
    stack = LinkedListStack[float]()
    assert stack.is_empty()
    stack.push(1.1)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()
