import num2words
import re

crimefile = open('covid_symptom.txt', 'r')
yourResult = [line.split('\n') for line in crimefile.readlines()]

inList = []
c = 0
for item in yourResult:
	c = c+1
	if c%2==0:
		item[0] = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), item[0])
		inList.append(item[0])

#print (inList)

inList2 = [i for i in inList if i != "****************************************"]
inList2 = list(set(inList2))
with open("covid_symptom_cleaned.txt", 'w') as output:
    for row in inList2:
        output.write(str(row) + '\n')