from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()

    def __repr__(self):
        elements = []

        for element in self.stack:
            elements.append(element)

        return " -> ".join(elements)

    def push(self, element):
        self.stack.appendleft(element)

    def pop(self):
        self.stack.popleft()

    def peek(self):
        return self.stack[0]

    def isEmpty(self):
        return len(self.stack) == 0

class Solution:
    openingsDict = { '(': ')', '[': ']', '{': '}' }
    closingsDict = { ')': '(', ']': '[', '}': '{' }

    def getClosing(self, item):
        return self.openingsDict[item]

    def isOpening(self, item):
        return item in self.openingsDict.keys()

    def isClosing(self, item):
        return item in self.closingsDict.keys()

    def isValid(self, s: str) -> bool:
        stk = Stack()
        if self.isOpening(s[0]):
            stk.push(s[0])
        else:
            return False
        for item in s[1:len(s)]:
            if self.isOpening(item):
                stk.push(item)
                continue

            elif not stk.isEmpty():
                if item == self.getClosing(stk.peek()):
                    stk.pop()
                    continue
                else:
                    return False
            else:
                if not stk.isEmpty(): continue
                return False
        return stk.isEmpty()


res = Solution()

tests = [
    "()",
    "(])",
    "(){}}{",
    "))"
]

for test in tests:
    print("Testing: `{}`".format(test))
    print(res.isValid(test))

