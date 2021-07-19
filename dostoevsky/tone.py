from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from top import res

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)
out = open('tone_txt.txt', 'w', encoding='utf8')

messages = open('C:/Users/yayar/OneDrive/Рабочий стол/b2/sonicDataAnalizeYaro/fetching_data/22_notes_fetched.txt', encoding='utf8').read().split('#')

results_tone = model.predict(messages, k=2)

for message, sentiment in zip(messages, results_tone):
    print('sentiment', sentiment)
    print(sentiment, file=out)
    print('results_tone',results_tone)
