from tone import results_tone
import csv

print('results_tone', results_tone)

header = ['positive', 'negative', 'neutral']

positive = []
neutral = []
negative = []

total_CSV = []
to_csv = [neutral, negative, positive]
for tone in results_tone:

    if 'neutral' in tone:
        neutral.append(tone['neutral'])
    else:
        neutral.append(0)

    if 'negative' in tone:
        negative.append(tone['negative'])
    else:
        neutral.append(0)
    if 'positive' in tone:
        positive.append(tone['positive'])
    else:
        positive.append(0)
with open('C:/Users/yayar/OneDrive/Рабочий стол/b2/sonicDataAnalizeYaro/csv/22DataTone.csv', 'w',
          newline='') as csvfile:
    sonic = csv.writer(csvfile, delimiter=',',
                       quotechar='|', quoting=csv.QUOTE_MINIMAL)

    data = list(zip(positive, negative, neutral))
    sonic.writerow(header)
    for row in data:
        row = list(row)
        sonic.writerow(row)

print("text_to_sentiment.py=> csv/22DataTone.csv")
