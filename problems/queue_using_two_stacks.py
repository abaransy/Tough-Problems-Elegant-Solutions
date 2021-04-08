# O(n) push and O(n) pop/peek
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)


    def pop(self, keep_front = False) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for i in range (len(self.s1)):
            ele1 = self.s1.pop()

            self.s2.append(ele1)

        ret = self.s2.pop()

        if keep_front:
            self.s2.append(ret)

        for i in range (len(self.s2)):
            ele2 = self.s2.pop()

            self.s1.append(ele2)

        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        ele = self.pop(True)

        return ele


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1

# O(1) push O(1) amortized pop
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2