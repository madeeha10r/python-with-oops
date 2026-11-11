class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c



obj = Calculator()


print("Addition of 2 numbers:", obj.add(10, 20))
print("Addition of 3 numbers:", obj.add(10, 20, 30))
print("Addition of 1 number:", obj.add(10))

