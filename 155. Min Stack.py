class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        if self.data:
            if x < self.data[-1][1]:
                self.data.append((x, x))
            else:
                self.data.append((x, self.data[-1][1]))
        else:
            self.data.append((x, x))

    def pop(self) -> None:
        return self.data.pop()[0]

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
