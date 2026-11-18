"""name=input("Enter your name")
age=input("Enter your age")
city=input("Enter your city")
print(f"Hello {name}, you are{age} years old and live in {city}")"""

"""num_str = input("Enter a number:")
num_int = int(float(num_str))
num_float = float(num_str)
num_complex = complex(num_str)
print("Int:",num_int,",Type:", type(num_int))
print("Float:",num_float,",Type:" type(num_float))
print("Complex:",num_complex,",Type:" type(num_complex))"""


"""num_str = input("Enter a number: ")

num_int = int(float(num_str))   # truncate after converting to float
num_float = float(num_str)
num_complex = complex(num_str)

print("Int:", num_int, ", Type:", type(num_int))
print("Float:", num_float, ", Type:", type(num_float))
print("Complex:", num_complex, ", Type:", type(num_complex))"""

#2 for arithmetic operators
"""a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
print("sum:",a+b)
print("difference",a-b)
print("quotient",a/b)
print("multiplication",a*b)"""

#Odd or even checker
"""num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")"""

#Multiplication Table
"""n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")"""

#Factorial finder
"""n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial",fact)"""

#Palindrome Checker
"""s=input("Enter a string: ")
if s==s [::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")"""

#list statistics
"""nums=[10,20,30,40,50]
print("Max:",max(nums))
print("Min:",min(nums))
print("Average",sum(nums)/len(nums))"""

#find prime numbers from (1,100)
"""for num in range(2,101):
    is_prime=True
    for i in range (2,int(num**0.5+1)):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num, end = " ")"""

#Sample Paper

"""name=input("Enter your name: ")
age=int(input("Enter your age; "))
city=input("Enter your city: ")
print(f"Hello {name} , you are {age} years old live in {city}")"""

"""n =123.45
a=int(n)
print(n)
print(type(n))
b=float(n)
print(n)
print(type(n))"""

"""Y=int(input("Enter Year: "))
if Y % 4==0 and Y % 100 !=0 or Y % 400 == 0:
    print("Leap Year")
else:
    print("Not a leap Year")"""

"""i=5
for n in range(1,7):
    print(f"{i}*{n}={i*n}")"""

"""def analyze_string(text):
    reversed_text = text[::-1]
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    return reversed_text, vowel_count

input_string = "Hello World"
reversed_str, count = analyze_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_str}")
print(f"Total Vowels: {count}")
print(f{"Original: {}"})"""

num_str=input()
num_int=int(float(num_str))
num_float=float(num_str)
num_complex=complex(num_float)
print("Int:",num_int,",Type:", type(num_int))
print("Float",num_float,",Type:", type(num_float))
print("Complex",num_complex,",Type:", type(num_complex))








