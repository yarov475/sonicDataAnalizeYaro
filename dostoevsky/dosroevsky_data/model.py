import gensim
from gensim.utils import simple_preprocess
import nltk
out = open('C:/Users/yayar/OneDrive/Documents/текст дисертации Ярочкин/публикации/sonicDataAnalizeYaro/dostoevsky/dosroevsky_data','w')
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('russian')
stop_words.extend(['в', 'на', 'и', 'не', 'за','b','евгения','михаиловна'])
def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc))
             if word not in stop_words] for doc in texts]
data = papper.text_processed.values.tolist()
data_words = list(sent_to_words(data))
# remove stop words
data_words = remove_stopwords(data_words)
print(data_words[:1][0][:30])