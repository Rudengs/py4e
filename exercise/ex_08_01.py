fHandle = open('mbox-short.txt')

for line in fHandle:
    line = line.strip()
    words = line.split()
    #print('Words', words)
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
