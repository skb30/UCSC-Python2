
"""
Scott Barth
Assignment 3 Part 1

The standard form of a quadratic expression is ax^2 + bx + c where a, b and c are real numbers and a is
 not equal to zero. The degree of a quadratic expression is 2 and a, b and c are called the
  coefficients. For example, in the quadratic expression (3x^2 + 8x − 5), the coefficients a, b, and
c are 3, 8 and -5 respectively. Define and use a Python class called ‘Quadratic’ that can perform
 operations on quadratic expressions such as addition and subtraction. The Python object that will
  create this class will be used as shown below:
Q1 = Quadratic(3,8,-5)
This corresponds to the expression above.
Define another Python object Q2 as follows
Q2 = Quadratic(2,3,7) which corresponds to the quadratic expression
2x^2 + 3x + 7

Part I – Addition and subtraction of quadratic expressions
Perform the addition and subtraction operation by using operator overloading. Make the following Python

calls:
quadsum = Q1+Q2
quaddiff = Q1-Q2
Print the values of quadsum and quaddiff. The output on your screen must be similar to the one below.
The sum is 5x^2+11x+2
The difference is x^2+5x-12

Part II – Equality operator for quadratic expressions
Two quadratic expressions are equal only if all the corresponding coefficients are equal. Define an
 equality operator that will return ‘True’ if two quadratic expressions are equal and ‘False’ when
  they are not equal. For example, in this code for Q1 == Q1, the value must be ‘True’ and for
   Q1 == Q2, the value must be ‘False'.


"""
class Quadratic():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c

        return str(a) + 'x^2' + ' + ' + str(b) +'x ' + str(c)

    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        c = self.c - other.c
        return str(a) + 'x^2' + ' + ' + str(b) + 'x ' + str(c)

    def __eq__(self, other):
        a = self.a == other.a
        b = self.b == other.b
        c = self.c == other.c

        if a and b and c == True:
            return True
        else:
            return False

q1 = Quadratic(3,8,-5)
q2 = Quadratic(2,3,7)

print(q1 + q2)
print(q1 - q2)
print(q1 == q1)
print(q1 == q2)


