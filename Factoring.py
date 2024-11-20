import sympy as sp

# The 150-bit number
num = 510143758735509025530880200653196460532653147

# Factorize the number
factors = sp.factorint(num)

# Get the smaller prime factor
smaller_prime = min(factors.keys())

# Print the smaller prime
print(f"The smaller prime is: {smaller_prime}")

