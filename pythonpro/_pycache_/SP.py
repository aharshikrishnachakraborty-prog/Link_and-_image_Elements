"""num_str=input()
num_int=int(float(num_str))
num_float=float(num_str)
num_complex=complex(num_float)
print("Int:",num_int,",Type:", type(num_int))
print("Float",num_float,",Type:", type(num_float))
print("Complex",num_complex,",Type:", type(num_complex))"""

num_str = input()

# Convert
num_int = int(float(num_str))   # truncate
num_float = float(num_str)
num_complex = complex(num_float)

print("Int:", num_int, ", Type:", type(num_int))
print("Float:", num_float, ", Type:", type(num_float))
print("Complex:", num_complex, ", Type:", type(num_complex))
