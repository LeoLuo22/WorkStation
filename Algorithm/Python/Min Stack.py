class MinStack:
    def __init__(self):
        self.s = []
        self.ms = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.s.append(x)
        if not self.ms:
            self.ms.append(x)
        elif x <= min(self.ms):
            self.ms.append(x)
        return x

    # @return nothing
    def pop(self):
        if not self.s:
            return
        stop = self.s[len(self.s) - 1]
        mstop = self.ms[len(self.ms) - 1]
        if stop == mstop:
            self.ms.pop()
        self.s.pop()

    # @return an integer
    def top(self):
        if not self.s:
            return 0
        return self.s[len(self.s) - 1]

    # @return an integer
    def getMin(self):
        if not self.ms:
            return 0
        return self.ms[len(self.ms) - 1]
