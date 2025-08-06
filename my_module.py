def is_even(number):
  """
  Returns true if the number is even. False if it's odd.
  example
  is_even(4) => True
  is_even(5) => False
  """
  return number % 2 == 0

def multiply_list(numbers):
  """
  multiplies all the numbers in a list and returns the product.
  example:
  multiply_list([2,3,4]) => 24
  """
  product = 1 
  for num in numbers:
    product *= num 
  return product 
