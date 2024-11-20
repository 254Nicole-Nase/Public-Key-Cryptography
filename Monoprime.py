from sympy import isprime, mod_inverse
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

# Given data from the challenge
N = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591
e = 65537
ct = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942

# Step 1: Factor N (for a single prime challenge)
# Using sympy to check if N is prime and factor if needed
from sympy import factorint

# Factor N
factors = factorint(N)
if len(factors) == 1:
    print(f"N is a prime number: {list(factors.keys())[0]}")
else:
    print(f"N is not prime, factors: {factors}")

# In the challenge, N should be prime.
# Step 2: Compute Euler's Totient
# phi(N) = N - 1 for prime modulus
phi_N = N - 1

# Step 3: Calculate the private key d
# d ≡ e^(-1) mod φ(N)
d = mod_inverse(e, phi_N)

# Step 4: Decrypt the ciphertext
# The ciphertext ct is a number, so we can use the modular exponentiation method to decrypt
decrypted = pow(ct, d, N)

# Step 5: Convert the decrypted value to bytes
flag = long_to_bytes(decrypted)

# Print the flag
print(f"Decrypted Flag: {flag.decode()}")
