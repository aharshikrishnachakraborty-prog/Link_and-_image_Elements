"""print('o----')  #o----
print(' ||||')  # ||||
price=10
print(price)
name=input('Enter your name: ')
print(f'Hello {name}') #1st Method
print('Hello ' + name) #2nd Method

name=input('Enter your name: ')
color=input('Enter your favorite color: ')
print(name +  ' likes '  + color) #Aharshi likes Pink
print(name + 'likes' + color) #AharshilikesPink
print(f'{name} likes {color}')"""#Aharshi likes Pink

"""birth_year=input('Enter your birth year: ')
age=2019-(birth_year)
print(age) #TypeError: unsupported operand type(s) for -: 'int' and 'str'

birth_year=input('Enter your birth year: ')
age=2019-int(birth_year)
print(age) #11

birth_year=int(input('Enter your birth year: '))
age=2019-birth_year
print(age)""" #11

"""weight_pounds=float(input('Enter your weight(in pounds): ')) #126
weight_kg= weight_pounds*0.45 #56.7
print(weight_kg)"""

course="Python for Beginners"
print(course.upper()) #PYTHON FOR BEGINNERS
print(course.lower()) #python for beginners
print(course.find('P')) #0
print(course.find('Beginners')) #11
print(course[2]) #t

