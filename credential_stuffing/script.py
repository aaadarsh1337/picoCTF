pairs = [x.strip() for x in open('creds-dump.txt', encoding='latin-1') if x]

for pair in pairs:
    print(pair.replace(';', ':'))
