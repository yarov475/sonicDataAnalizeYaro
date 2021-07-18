from tone import results_tone
import csv


print('results_tone', results_tone)

header = ['positive', 'negative', 'neutral']

positive = []
neutral = []
negative = []

total_CSV = []
to_csv = [neutral, negative, positive]
for dic in results_tone:

    if 'neutral' in dic:
        neutral.append(dic['neutral'])

    if 'negative' in dic:
        negative.append(dic['negative'])
    if 'positive' in dic:
        positive.append(dic['positive'])

# print('lists', positive, negative, neutral)

with open('../csv/tone_text_data.csv', 'w', newline='') as csvfile:
    sonic = csv.writer(csvfile, delimiter=',',
                       quotechar='|', quoting=csv.QUOTE_MINIMAL)

    data = list(zip(positive, negative, neutral))
    sonic.writerow(header)
    for row in data:
        row = list(row)
        sonic.writerow(row)

# with open('../csv/tone_topic_data_to_sc_1.csv', 'w', newline='') as csvfile:
#     sonic = csv.writer(csvfile, delimiter=',',
#                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
#
#     data = list(zip(positive, negative, neutral))
#
#     for row in data:
#         row = list(row)
#         sonic.writerow(row)

print("Program sonic tone completed")
