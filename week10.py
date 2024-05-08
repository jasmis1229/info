class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f'{self.a} + {self.b}i'
    
    
A=Complex(1, 2)
B=Complex(3, 4)
print(A+B)
print(A-B)
print(A*B)