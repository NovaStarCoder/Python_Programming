import math

def check_armstrong(number):
  """Return True if a number is Armstrong otherwise Return False"""
  res_sum,k = 0,0
  while(k):
    res_sum += math.factorial(k%10)
    k //= 10
  if res_sum == number:
    return True
  return False
  
  
  
if __name__ == "__main__":
  n = int(input())
  if check_armstrong(n):
    print("{} is Armstrong.".format(n))
  else:
    print("{} is Not Armstrong.".format(n))
