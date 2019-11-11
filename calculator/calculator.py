from calculator.addition import addition
from calculator.subtract import subtraction
from calculator.division import division
from calculator.multiplication import multiplication
from calculator.square import square
from calculator.squareRoot import squareRoot


class Calculator(object):
    result = None

    def __init__(self):
        result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def sqr(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = squareRoot(a)
        return self.result
