fHandle = open('mbox-short.txt')

for line in fHandle:
    line = line.rstrip()
    print(line.upper())
