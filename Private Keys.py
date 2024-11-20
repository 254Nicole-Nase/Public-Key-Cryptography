# Given values
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Calculate Euler's Totient function phi(N)
phi_N = (p - 1) * (q - 1)

# Function to compute modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Compute the private key d
d = mod_inverse(e, phi_N)

# Print the private key
print(d)
