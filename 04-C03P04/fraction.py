class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.

        If denominator = 0, raise ValueError.
        """
        if denominator == 0:
            raise ValueError("I can't divide by zero")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """
        Returns the string representation of self.
        """
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """
        return isinstance(other, self.__class__)

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if self.denominator == other.denominator:
            new_numerator = self.numerator + other.numerator
            return f"{new_numerator}/{self.denominator}"
        else:
            new_denominator = self.denominator * other.denominator
            new_numerator = ((self.numerator * other.denominator)
                            + (other.numerator * self.denominator))
            return f"{new_numerator}/{new_denominator}"

    def __sub__(self, other):
        """
        Returns new Fraction, that's the subtraction of self and other.
        """
        if self.denominator == other.denominator:
            new_numerator = self.numerator - other.numerator
            return f"{new_numerator}/{self.denominator}"
        else:
            new_denominator = self.denominator * other.denominator
            new_numerator = ((self.numerator * other.denominator)
                            - (other.numerator * self.denominator))
            return f"{new_numerator}/{new_denominator}"

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return f"{new_numerator}/{new_denominator}"

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        new_numerator = self.numerator
        new_denominator = self.denominator
        result = ''

        while Fraction(new_numerator, new_denominator).is_simplified():
            num = new_numerator
            while num > 1:
                if new_numerator % num == 0 and new_denominator % num == 0:
                    result = f"{int(self.numerator/num)}/{int(self.denominator/num)}"
                    break
                num -= 1
            new_numerator /= num
            new_denominator /= num
        return result

    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
        num = self.numerator
        while num > 1:
            if self.numerator % num == 0 and self.denominator % num == 0:
                return True
            num -= 1
        return False
