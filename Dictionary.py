fName = input("Please Enter File Name:")
fContent = open(fName)
senderDict = dict()
for line in fContent:
    if not line.startswith("From "):
        continue
    words = line.split()
    senderDict[words[1]] = senderDict.get(words[1], 0) + 1

bigWord = None
bigCount = None
for word,count in senderDict.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print(bigWord, bigCount)
