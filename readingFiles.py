
from urllib.request import Request, urlopen

request = Request(
    url = 'https://www.py4e.com/code3/mbox-short.txt',
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}
) 

encoding = 'utf-8'
webpage = str(urlopen(request).read(),encoding).split('\n')

floatValues = []


# print(webpage)
for line in webpage:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    startStr = line.find('0')
    floatNumber = float(line[startStr:])
    floatValues.append(floatNumber)    
    total = 0
    for floatNumber in floatValues:
        total += floatNumber
    count = len(line) + 1
averageNumber = total / count

print(f'Average spam confidence: '+str(averageNumber))