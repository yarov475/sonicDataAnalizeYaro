from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)
prepared_data = open('prepared_data.py', encoding='utf8').read().split('\n')

print(type(prepared_data[0]))
out = open('msg_sent.txt',  'w', encoding='utf8')
messages = prepared_data[0].replace('[', '').replace('\'', '').split(',')
results = model.predict(messages, k=2)
for message, sentiment in zip(messages, results):
    print(sentiment)
    print(sentiment, file=out)
