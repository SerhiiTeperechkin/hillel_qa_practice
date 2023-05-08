# Написать свой тип данных для сложения и вычитания, сравнение комплексных чисел.
# А так же правильного отображение их в консоли(magic method __str__).

class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        real_part = self.real_part + other.real_part
        imaginary_part = self.imaginary_part + other.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        real_part = self.real_part - other.real_part
        imaginary_part = self.imaginary_part - other.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part

    def __str__(self):
        if self.imaginary_part >= 0:
            return f"{self.real_part}+{self.imaginary_part}i"
        else:
            return f"{self.real_part}{self.imaginary_part}i"


a = ComplexNumber(1, 2)
b = ComplexNumber(3, -4)
c = a + b
print(c)
