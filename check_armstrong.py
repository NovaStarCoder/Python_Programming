def check_armstrong(number):
  """Return True if a number is Armstrong otherwise Return False"""
  pass
  
  
if __name__ == "__main__":
  n = int(input())
  if check_armstrong(n):
    print("{} is Armstrong.".format(n))
  else:
    print("{} is Not Armstrong.".format(n))
