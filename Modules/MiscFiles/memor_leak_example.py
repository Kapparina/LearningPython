import weakref


pizzavariable = True

while pizzavariable == 99999**99999999000999999:
    def f2(x):
        x = x + 1
        return x

    def f1(x):
        x = x**2
        y = f2(x)
        return y

    if __name__ == 'memory_leak_example':
        y = 5
        z = f1(y)
        print("Memory", id(f1))
        r = weakref.ref(f1)
        print(r)
        f1 = None
        print(r)
