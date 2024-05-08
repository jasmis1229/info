class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

A = Complex(1, 2)
B = Complex(3, 4)
print(A + B)
print(A - B)
print(A * B)
