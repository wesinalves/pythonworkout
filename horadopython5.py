class Complex():
  def __init__(self, real_part=1, imaginary_part=1):
    self.real = real_part
    self.imaginary = imaginary_part    
  
  def add(self, complex):
    r = self.real + complex.real
    im = self.imaginary + complex.imaginary
    return Complex(r, im)
  
  def subtract(self, complex):
    r = complex.real - self.real
    im = complex.imaginary - self.imaginary
    return Complex(r, im)
  
  def echo(self):
    print(f'({self.real},{self.imaginary})')


############################################################


class RationalNumber():
  def __init__(self, numerator=1, denominator=2):
    self.num = numerator
    self.den = denominator

  def add(self, number):
    if number.den == self.den:
      numerator = self.num + number.num
      return RationalNumber(numerator, self.den)
    else:
      denominator = self._lcm(self.den, number.den)
      numerator = (
          ((denominator // self.den) * self.num) 
          + ((denominator // number.den) * number.num)
      )
      rational = RationalNumber(numerator, denominator)
      rational.simplify()
      return rational
  
  def subtract(self, number):
    if number.den == self.den:
      numerator = self.num - number.num
      return RationalNumber(numerator, self.den)
    else:
      denominator = self._lcm(self.den, number.den)
      numerator = (
          ((denominator // self.den) * self.num)
          - ((denominator // number.den) * number.num)
      )
      rational = RationalNumber(numerator, denominator)
      rational.simplify()
      return rational
  
  def multiply(self, number):
    numerator = self.num * number.num
    denominator = self.den * number.den
    rational = RationalNumber(numerator, denominator)
    rational.simplify()
    return rational
  
  def divide(self, number):
    numerator = self.num * number.den
    denominator = self.den * number.num
    rational = RationalNumber(numerator, denominator)
    rational.simplify()
    return rational

  def echo(self):
    print(f'{self.num}/{self.den}')
  
  def result(self):
    print(self.num / self.den)

  def simplify(self):
    gcd = self._gcd(self.num, self.den)
    self.num = self.num // gcd
    self.den = self.den // gcd
  
  def _lcm(self, number1, number2):
    minimum = min(number1, number2)
    
    while(True):
      if minimum % number1 == 0 and minimum % number2 == 0:
        return minimum
      else:
        minimum += 1

  def _gcd(self, number1 , number2):
    largest = min(number1,number2)
    while(True):
      if number1 % largest == 0 and number2 % largest == 0:
        return largest
      else:
        largest -= 1