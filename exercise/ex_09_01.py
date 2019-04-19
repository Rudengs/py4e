fName = input("Enter file name: ")
if len(fName) < 1 : fName = 'clown.txt'
fHandle = open(fName)

wordDic = dict()
for line in fHandle:
    words = line.split()
    for word in words:
        wordDic[word] = wordDic.get(word, 0) + 1

bigCount = None
bigWord = None

for word, count in wordDic.items():
    if bigCount == None or bigCount < count:
        bigCount = count
        bigWord = word

print(bigWord, bigCount)
