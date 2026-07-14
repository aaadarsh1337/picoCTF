from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
 
time = 1770242624
ciphertext = "dcc2a6a4cf3dbc69a929aa7c4e3c33e7558eef1f2244bde76e450b065188db38"
 
def decrypt(ciphertext: str, timestamp: int) -> str:
    key = sha256(str(timestamp).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(ciphertext))
    return unpad(decrypted, AES.block_size).decode()
 
plaintext = decrypt(ciphertext, time)
print(plaintext)

