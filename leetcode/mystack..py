#python3
#use queue to realize stack
import collections

class MyStack:
    def __init__(self):
        self.queue = collections.deque()
    def push(self,x) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for i in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]
    
    def empty(self) -> bool:
        return not self.queue
