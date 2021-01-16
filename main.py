

print ("""
1) ADDITION 
2) SUBTRACTION 
3) MULTIPLICATION
4) DIVISION
5) SQUARE ROOT 
""")

user_input = int (input ("enter the number : "))

def calculator ():
  
   checking ()



def multiplication ():
  user_choice1 = int (input ('enter the frist number : '))
  user_choice2 = int (input ("enter the number 2 :"))    

  def a (x):
    return (lambda y :x*y)

  s = a (user_choice1)
  print (s(user_choice2))
  

def addition ():
  user_choice1 = int (input ('enter the frist number : '))
  user_choice2 = int (input ("enter the number 2 :"))    

  def a (x):
    return (lambda y :x+y)

  s = a (user_choice1)
  print (s(user_choice2))
  
def subtraction ():
  user_choice1 = int (input ('enter the frist number : '))
  user_choice2 = int (input ("enter the number 2 :"))    

  def a (x):
    return (lambda y :x-y)

  s = a (user_choice1)
  print (s(user_choice2))
  
def division ():
  user_choice1 = int (input ('enter the frist number : '))
  user_choice2 = int (input ("enter the number 2 :"))    

  def a (x):
    return (lambda y :x//y)

  s = a (user_choice1)
  print (s(user_choice2))

def squareroot ():
  square_num = int (input ("enter the number : "))

  square = lambda a: a*a
  print (square(square_num))
  
def checking ():
  numbers = 1,2,3,4,5
  
  if user_input == 1:
    print ("you choosed addition ")
    addition ()

  elif user_input == 2 :
    print ("you choosed subtraction")
    subtraction ()

  elif user_input == 3 :
    print ("you choosed the multiplication ")
    multiplication ()

  elif user_input == 4 :
    print ("you choosed the division")
    division () 

  elif user_input == 5 :
    print ('you choosed ROOT ')
    squareroot()
 
  elif user_input not in numbers :
    print ("enter the correct number")



calculator ()