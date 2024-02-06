class MyQueue(object):

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1] if self.outStack else None

    def empty(self):
        """
        :rtype: bool
        """
        return not self.inStack and not self.outStack


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
