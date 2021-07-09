from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)
prepared_data = open('prepared_data.txt', encoding='utf8').read().split('\n')
print(prepared_data)
out = open('msg_sent.txt',  'w', encoding='utf8')
messages = prepared_data
results = model.predict(messages, k=2)

for message, sentiment in zip(messages, results):
    print(sentiment, file=out)
