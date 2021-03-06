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
        if self.numerator == 0:
            return '0'

        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """
        is_instance = isinstance(other, self.__class__)
        if not is_instance:
            raise TypeError('ATTENTION: can only be compared if both objects are a class Fraction')
        simplify_class = self.simplify()
        simplify_other = other.simplify()
        is_equal_numerators = simplify_class.numerator == simplify_other.numerator
        is_equal_denominator = simplify_class.denominator == simplify_other.denominator

        return is_instance and is_equal_numerators and is_equal_denominator

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if self.denominator == other.denominator:
            new_numerator = self.numerator + other.numerator
            return Fraction(new_numerator, self.denominator)

        new_denominator = self.denominator * other.denominator
        new_numerator = ((self.numerator * other.denominator)
                            + (other.numerator * self.denominator))
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Returns new Fraction, that's the subtraction of self and other.
        """
        if self.denominator == other.denominator:
            new_numerator = self.numerator - other.numerator
            return Fraction(new_numerator, self.denominator)

        new_denominator = self.denominator * other.denominator
        new_numerator = ((self.numerator * other.denominator)
                            - (other.numerator * self.denominator))
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __lt__(self, other):
        """
        Returns True/False if self is lower to other.
        """
        self_fraction_value = self.numerator / self.denominator
        other_fraction_value = other.numerator / other.denominator
        return self_fraction_value < other_fraction_value

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        new_numerator = self.numerator
        new_denominator = self.denominator
        result = Fraction(new_numerator, new_denominator)

        while not Fraction(new_numerator, new_denominator).is_simplified():
            num = new_numerator
            while num > 1:
                if new_numerator % num == 0 and new_denominator % num == 0:
                    result = Fraction(int(self.numerator/num), int(self.denominator/num))
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
                return False
            num -= 1
        return True

    @staticmethod
    def sorted(fractions):
        fractions_tuples = []
        for fraction in fractions:
            fraction_value = fraction.numerator / fraction.denominator
            fractions_tuples.append((fraction_value, fraction))
        sorted_tuples = sorted(fractions_tuples, key=lambda fract_value: fract_value[0])

        return [sort_frac[1] for sort_frac in sorted_tuples]
