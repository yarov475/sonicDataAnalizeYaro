import pandas as pd
import re
import gensim
from gensim.utils import simple_preprocess
import nltk




paper = pd.read_csv(
    'C:/Users/yayar/OneDrive/Documents/текст дисертации Ярочкин/публикации/sonicDataAnalizeYaro/.ipynb_checkpoints/22Data.csv',
    delimiter=',')
papper = all[['text']]


# Remove punctuation
papper['text_processed'] = \
    papper['text'].map(lambda x: re.sub('[,\.!?]', '', x))
# Convert the titles to lowercase
papper['text_processed'] = \
    papper['text_processed'].map(lambda x: x.lower())
# Print out the first rows of papers
papper['text_processed'].head()

out = open(
    'C:/Users/yayar/OneDrive/Documents/текст дисертации Ярочкин/публикации/sonicDataAnalizeYaro/dostoevsky/dosroevsky_data/row.txt',
    'w', encoding='utf8')
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('russian')
stop_words.extend(['в', 'на', 'и', 'не', 'за', 'b', 'евгения', 'михаиловна'])


def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))


def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc))
             if word not in stop_words] for doc in texts]


data = papper.text_processed.values.tolist()
data_words = list(sent_to_words(data))
# remove stop words
data_words = remove_stopwords(data_words)
print(data_words[:1][0][:30], file=out)
