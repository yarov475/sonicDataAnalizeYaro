from app import results
import csv

heder = ['neutral', 'negative', 'positive']
neutral = []
negative = []
positive = []
to_csv = [ neutral, negative, positive]
for dic in results:
    if 'neutral' not in dic:
        neutral.append(0)
    else:
        neutral.append(dic['neutral'])
    if 'negative' not in dic:
        negative.append(0)
    else:
        negative.append(dic['negative'])
    if 'positive' not in dic:
        positive.append(0)
    else:
        positive.append(dic['positive'])

print(neutral, negative, positive)
to_csv = [heder, neutral, negative, positive]
print('to_csv', to_csv)

myFile = open('example2.csv', 'w')

with myFile:
    writer = csv.writer(myFile)
    writer.writerows(to_csv)

print("Writing complete")


