# Given values
N = 882564595536224140639625987659416029426239230804614613279163
c = 77578995801157823671636298847186723593814843845525223303932

# Private key d from previous challenge
d = 121832886702415731577073962957377780195510499965398469843281  # Replace this with the private key 'd' you obtained earlier

# Perform modular exponentiation to decrypt the message
m = pow(c, d, N)

# Print the decrypted message
print(m)
