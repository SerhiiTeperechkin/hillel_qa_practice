# Написать свой тип данных для сложения и вычитания, сравнение комплексных чисел.
# А так же правильного отображение их в консоли(magic method __str__).

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

# [FIXED] Хотелось бы еще видеть проверку, что other является инстансом класса ComplexNumber
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imaginary = self.imaginary + other.imaginary
            return ComplexNumber(real, imaginary)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imaginary = self.imaginary - other.imaginary
            return ComplexNumber(real, imaginary)
        else:
            raise TypeError("Unsupported operand type for -")

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        else:
            return False

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"


if __name__ == '__main__':
    a = ComplexNumber(2, 3)
    b = ComplexNumber(1, 4)
    c = 5

    result = a + b
    print(result)

    result = a + c  # Будет вызвано исключение TypeError

    result = a - b
    print(result)

    result = a - c  # Будет вызвано исключение TypeError
