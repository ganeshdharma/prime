# import math
#
# def is_prime(n=10):
#      if n>2 :
#        return False
#
#      for i in range (2, int(math.sqrt(n))):
#         if n % i == 0:
#           return False
#
#      return True

# def PrimeChecker(a):
#     # Checking that given number is more than 1
#     if a > 1:
#         # Iterating over the given number with for loop
#         for j in range(2, int(a/2) + 1):
#             # If the given number is divisible or not
#             if (a % j) == 0:
#                 print(a, "is not a prime number")
#                 break
#         # Else it is a prime number
#         else:
#             print(a, "is a prime number")
#     # If the given number is 1
#     else:
#         print(a, "is not a prime number")
# # Taking an input number from the user
# a = int(input("Enter an input number:"))
# # Printing result
# PrimeChecker(a)
l = 10
u = 20

for num in range(l, u + 1):
    print(num);