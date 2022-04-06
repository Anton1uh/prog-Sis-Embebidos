class Series_and_strings:

    def __init__(self):
        n = None

    def fibonacci(self):
        n = int(input("Ingresa N: "))
        n1 = 0
        n2 = 1
        aux = 0
        print("Secuencia:")
        while aux < n:
            print(n1)
            r = n1 + n2
            n1 = n2
            n2 = r
            aux += 1
    def factorial(self):
        n = int(input("Ingresa N: "))
        Factorial = 1
        for i in range(1, n + 1):
            Factorial = Factorial * i
        print("El factorial", n, "es", Factorial)


Series_and_strings1 = Series_and_strings()
Series_and_strings1.fibonacci()
##Series_and_strings1.factorial()


