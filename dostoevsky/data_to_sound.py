from app import results
import csv

header = ['positive', 'negative', 'neutral']
mlt = 1000
positive = []
neutral = []
negative = []

total_CSV = []
to_csv = [neutral, negative, positive]
for dic in results:

    if 'neutral' in dic:
        neutral.append(dic['neutral'] * mlt)

    if 'negative' in dic:
        negative.append(dic['negative'] * mlt)
    if 'positive' in dic:
        positive.append(dic['positive'] * mlt)
    # else:
    #     total_CSV.append(0)
print('lists', positive, negative, neutral)

with open('../csv/tone_topic_data.csv', 'w', newline='') as csvfile:
    sonic = csv.writer(csvfile, delimiter=',',
                       quotechar='|', quoting=csv.QUOTE_MINIMAL)

    data = list(zip(positive, negative, neutral))
    sonic.writerow(header)
    for row in data:
        row = list(row)
        sonic.writerow(row)

with open('../csv/tone_topic_data_to_sc.csv', 'w', newline='') as csvfile:
    sonic = csv.writer(csvfile, delimiter=',',
                       quotechar='|', quoting=csv.QUOTE_MINIMAL)

    data = list(zip(positive, negative, neutral))

    for row in data:
        row = list(row)
        sonic.writerow(row)

print("Program sonic  completed")
