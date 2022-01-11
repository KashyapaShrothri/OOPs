class mathMod:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def average(x, y):
        return mathMod.add(x, y) / 2


print(mathMod.average(10, 20))
