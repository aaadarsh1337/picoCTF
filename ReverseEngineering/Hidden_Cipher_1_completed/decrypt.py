from pwn import *

key = b'S3Cr3t'
encrypted = bytes.fromhex("235a201d702015483b1d412b265d3313501f0c072d135f0d2002302d57113700761357102e")

print(xor(encrypted, key).decode())
