from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

messages = [
    ' день',
'воиска',
'города',
'воина',
'дома',
'наши',
'дома',
'день',
'дома',

]

results = model.predict(messages, k=2)
for message, sentiment in zip(messages, results):
    print(message, '->', sentiment)
