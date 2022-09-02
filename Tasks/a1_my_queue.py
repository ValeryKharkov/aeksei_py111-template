"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        ...  # todo для очереди можно использовать python list
        self.data = []
        self.index = 0

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.data.append(elem)
        self.index += 1

        print(elem)
        #print(f"index = {self.index}")
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        self.data.pop(0)
        self.index -= 1
        return None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        print(ind)
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        return None

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.data)

    q.dequeue()
    #q.dequeue()
    #q.dequeue()
    #q.dequeue()
    print(q.data)
