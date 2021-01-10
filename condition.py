# this code has one condition only [ if ]

num = 5

if num > 2:
  # if the condition is true will exicute the following block
  print('num > 2')
  print('this code created by abdulrahman'.title())
  


# this code has to condition [ if and else ]
number = 12

# the following code will exixuit if the condition is true
if number == 12:
  print('number = 12')

else:
  print('number is not less than 12')

# this code has 3 conditions [ if elif and else ]

# this cond will cheack the first condition if it is true then wll
# exicuit the code side the if block otherwise will check the elif
# f the condition is true will exuit the code inside the elif
# last if all the above conditions are not true will exuciuts the else
# block

# not the code exicuit from up to down
# we used  if only once in the code
# we can use elif as many as we need
# else used only once which will exicuit if all the condions are false


if number < 23:
  print('number < 23')
elif number == 23:
  print('number = 23')
else:
  print('number should be greater than 23')


# using nested if in python

# the follwing code using nested if to cheak the student
# grad for math and print out the GPA

grad = float( input('enter your math\'s grad: '.title()) )


if grad >= 50:
  print('conggratulation you pass;'.title())
  if grad >= 90:
    print('Your GPA is A*')
  elif grad > 80:
    print('Your GPA is A')
  elif grad >= 70:
    print('Your GPA is B*')
  elif grad >= 60:
    print('Your GPA is B')
  else:
    print('Your GPA is C')
else:
  print('sorry, your failed'.title())
print()
print()


# using ternery operators
# ternery operator  used for a short term [ has if only or if and else and not use it with 3 conditions]

x = 5

# using erenery operator 
print('x = 5') if x == 5 else print('x != 5')



# using [ all( means and all the condition shoult be true)]
# any means or one of the condition should be true to exicuit the code

num1 = int( input('enter number1: '.title() ) )
num2 = int( input('enter number2: '.title() ) )
num3 = int( input('enter number3: '.title() ) )
num4 = int( input('enter number4: '.title() ) )


# in this case wll print all done in upper case if all is True 
if all([ num1 == 2, num2 == 3, num3 == 1, num4 == 0]):
  print('all done'.upper() )
  
elif any([num1 == 1, num2 > 12, num3 == 0, num4 ==  -2]):
  print('not all done'.upper() )



# to check if some think is in list, tupple, dict or even string
# to check of some think is park of

numbers = [1,2,3,4,5,6,7,8,9]

if 10 in numbers:
  print('found'.upper() )
else:
  print('not found'.upper())

# not operator
# not operators used to inverte the value
# if the condition if True will invert to False
# if the condition if False will invert to True


# this the user input and the compiler will read it
userInput = int( input('> ') )

# this part will check of the condition is True or False and the wil invert it due to using not operator
# if the condition is True it will invert to False and is the condition is False will invert to True

if not userInput == 12:
  print('true'.upper() )
else:
  print('false'.upper ())

