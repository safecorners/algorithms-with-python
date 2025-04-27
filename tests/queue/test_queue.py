from queue.queue import Queue


def test_enqueue_and_dequeue() -> None:
    queue = Queue[str]()

    queue.enqueue("dog")
    queue.enqueue("cat")
    queue.enqueue("pig")

    assert queue.dequeue() == "dog"
    assert queue.dequeue() == "cat"
    assert queue.dequeue() == "pig"
    assert queue.dequeue() is None
