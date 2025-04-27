from stack.array_stack import ArrayStack


def test_push_and_pop() -> None:
    stack = ArrayStack[int]()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.pop() is None
    assert stack.size() == 0


def test_peek() -> None:
    stack = ArrayStack[str]()
    assert stack.peek() is None
    stack.push("x")
    assert stack.peek() == "x"
    stack.push("y")
    assert stack.peek() == "y"
    stack.pop()
    assert stack.peek() == "x"


def test_is_empty() -> None:
    stack = ArrayStack[float]()
    assert stack.is_empty()
    stack.push(1.5)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()
