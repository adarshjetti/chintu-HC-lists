# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class Dhruva(Exception):
    def __init__(self,value="snowflake"):
        self.value = value
    def __str__(self):
        return(repr(self.value))

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise Dhruva
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print("DHRUVA")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
   except Dhruva as d:
        print('A New Exception occured: '+d.value)
        print("Dhruva is a star")

print("Congratulations! You guessed it correctly.")

try:
    a="Cat"
    b=3
    print(a+b)
except :
    print("yuppie")