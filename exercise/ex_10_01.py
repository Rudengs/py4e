fName = input("Enter file name: ")
if len(fName) < 1 : fName = 'clown.txt'
fHandle = open(fName)

wordDic = dict()
for line in fHandle:
    words = line.split()
    for word in words:
        wordDic[word] = wordDic.get(word, 0) + 1

temp = sorted( [ (v, k) for k,v in wordDic.items() ] ,reverse=True )

for v,k in temp[:5] :
    print(k,v)
