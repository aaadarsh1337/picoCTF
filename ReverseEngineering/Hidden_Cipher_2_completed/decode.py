with open('test', 'r') as f:
    while ":" not in f.readline(1):
        f.readline(1)
    encoded = f.read().strip()

codelist = encoded.split(', ')

for letter in codelist:
    ascicode = int(letter) // 3
    print(chr(ascicode), end='')
