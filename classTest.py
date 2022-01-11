# Function defined outside the class
def f1(self, x, y):
    return min(x, x - y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


obj = C()
print(dir(obj))

print(obj.f(1, 3))
print(obj.h())
