fName = input("Please Enter File Name:")
fContent = open(fName)
hourDict = dict()
for line in fContent:
    if not line.startswith("From "):
        continue
    words = line.split()
    timeElements = words[5].split(":")
    hour = timeElements[0]
    hourDict[hour] = hourDict.get(hour, 0) + 1

for hour,count in sorted(hourDict.items()):
    print(hour,count)
