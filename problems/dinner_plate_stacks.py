# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

# Implement the DinnerPlates class:

# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
# void push(int val) Pushes the given positive integer val into the leftmost stack with size less than capacity.
# int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
# int popAtStack(int index) Returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vacant_dishes = set([i ])

    def push(self, val: int) -> None:


    def pop(self) -> int:


    def popAtStack(self, index: int) -> int:
