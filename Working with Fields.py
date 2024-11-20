def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(g, p):
    g, x, y = extended_gcd(g, p)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % p

# Given values
g = 209
p = 991

# Calculate the modular inverse
d = mod_inverse(g, p)

print(f"The modular inverse of {g} modulo {p} is: {d}")
