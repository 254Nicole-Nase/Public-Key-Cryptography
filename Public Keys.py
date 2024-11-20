# Given values
message = 12
e = 65537
p = 17
q = 23

# Calculate modulus N
N = p * q

# Calculate ciphertext
ciphertext = pow(message, e, N)

# Print the result
print(ciphertext)
