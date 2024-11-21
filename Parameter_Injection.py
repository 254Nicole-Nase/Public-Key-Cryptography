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
    print("[*] Attempting to connect to socket.cryptohack.org on port 13371")
    io = remote("socket.cryptohack.org", 13371)
    io.readline()
except Exception as e:
    print(f"[!] Error: Could not connect to socket.cryptohack.org on port 13371: {e}")
    sys.exit(1)

try:
    # Send initial data to the server
    print("[*] Sending initial data to the server")
    io.sendline(dumps({"p":"0x123", "g":"0x123", "A":"0x123"}).encode())
    io.readline()

    # Send B = 1 to the server
    print("[*] Sending B = 1 to the server")
    io.sendline(dumps({"B":"0x01"}).encode())
    io.readuntil(b"from Alice: ")
    recv = loads(io.readline())
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
print(decrypt_flag(shared_secret, iv, ciphertext))