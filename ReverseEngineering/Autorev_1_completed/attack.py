from pwn import *

host = 'mysterious-sea.picoctf.net'
port = 60328

conn = remote(host, port)

conn.recvline()
key = conn.recvline().strip()
conn.recvuntil(b"What's the secret?")
conn.recv()
conn.sendline(key)

for i in range(2, 21):
    conn.recvuntil(b'Correct!\n')
    key = conn.recvline().strip()
    print(key)
    conn.recvuntil(b"What's the secret?:")
    conn.sendline(key)

conn.interactive()
