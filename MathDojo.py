class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
            self.result -= x
        return self


md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

md1 = MathDojo()
y = md1.add(3).add(10,5,1).subtract(3,3).result
print(y)

md2 = MathDojo()
y = md2.add(3).add(10,5,1,6).subtract(3).result
print(y)


