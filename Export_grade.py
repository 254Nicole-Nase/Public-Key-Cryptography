from Crypto.Util.Padding import unpad
from json import loads, dumps
from Crypto.Cipher import AES
from hashlib import sha1
from pwn import remote, context
import sys

def decrypt_flag(shared_secret, iv, ciphertext):
    key = sha1(str(shared_secret).encode()).digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)
    return plaintext.decode()

try:
    # Attempt to connect to the remote server
    print("[*] Attempting to connect to socket.cryptohack.org on port 13379")
    io = remote("socket.cryptohack.org", 13379)
    io.readline()
except Exception as e:
    print(f"[!] Error: Could not connect to socket.cryptohack.org on port 13379: {e}")
    sys.exit(1)

try:
    # Send initial data to the server
    print("[*] Sending initial data to the server")
    initial_data = {"p": "0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1",
                    "g": "0x2",
                    "A": "0x1234567890ABCDEF"}
    io.sendline(dumps(initial_data).encode())
    response = io.readline()
    print(f"[*] Initial data response: {response}")

    # Send B = 1 to the server
    print("[*] Sending B = 1 to the server")
    io.sendline(dumps({"B": "0x01"}).encode())
    io.readuntil(b"from Alice: ")
    recv = loads(io.readline())
    print(f"[*] Received data: {recv}")
except Exception as e:
    print(f"[!] Error during communication: {e}")
    sys.exit(1)

# Extract IV and ciphertext from the received data
iv, ciphertext = recv["iv"], recv["encrypted_flag"]

# Decrypt the flag using the shared secret
shared_secret = 1
try:
    decrypted_flag = decrypt_flag(shared_secret, iv, ciphertext)
    print(f"[*] Decrypted flag: {decrypted_flag}")
except Exception as e:
    print(f"[!] Error during decryption: {e}")
    sys.exit(1)