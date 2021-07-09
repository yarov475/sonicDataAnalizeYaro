import pandas as pd


#%%

import matplotlib.pyplot as plt

#%%

from matplotlib import pyplot

#%%

all = pd.read_csv('C:/Users/yayar/OneDrive/Documents/текст дисертации Ярочкин/публикации/sonicHist/22Data.csv',delimiter=',')

#%%


all = pd.read_csv('C:/Users/yayar/OneDrive/Documents/текст дисертации Ярочкин/публикации/sonicHist/22Data.csv',delimiter=',')

#%%

display(all)

#%%

tone = pd.read_csv('22DataTone.csv',delimiter=',')

#%%

display(tone)

#%%

index = tone["+"]
values = tone['-']
plt.bar(index,values)
plt.show()

#%%

from matplotlib import pyplot

pyplot.axis('equal')
tone['0'].plot(kind='pie')

#%%

tone['0'].hist()
tone['+'].hist()
tone['-'].hist()



#%%

index = tone["+"]
values = tone['0']
plt.bar(index,values)
plt.show()

#%%

простая гистограмма до соноризации

#%%

import os

#%%

os.chdir('..')

#%%

paper =  pd.read_csv('C:/Users/yayar/OneDrive/Documents/текст дисертации Ярочкин/публикации/sonicHist/22Data.csv',delimiter=',')

#%%

papper = all[['text']]


#%%

papper.head()



#%%

import re

# Remove punctuation
papper['text_processed'] = \
papper['text'].map(lambda x: re.sub('[,\.!?]', '', x))
# Convert the titles to lowercase
papper['text_processed'] = \
papper['text_processed'].map(lambda x: x.lower())
# Print out the first rows of papers
papper['text_processed'].head()

#%%



#%%

# Import the wordcloud library
from wordcloud import WordCloud
# Join the different processed titles together.
long_string = ','.join(list(papper['text_processed'].values))
# Create a WordCloud object
wordcloud = WordCloud(background_color="black", max_words=5000, contour_width=3, contour_color='steelblue')
# Generate a word cloud
wordcloud.generate(long_string)
# Visualize the word cloud
wordcloud.to_image()

#%%

import gensim
from gensim.utils import simple_preprocess
import nltk
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


#%%

import gensim.corpora as corpora
# Create Dictionary
id2word = corpora.Dictionary(data_words)
# Create Corpus
texts = data_words
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
# View
print(corpus[:1][0][:30])

#%%

from pprint import pprint
# number of topics
num_topics = 10
# Build LDA model
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics)
# Print the Keyword in the 10 topics
pprint(lda_model.print_topics())
doc_lda = lda_model[corpus]

#%%



#%%

import pyLDAvis.gensim
import pickle
import pyLDAvis
# Visualize the topics
pyLDAvis.enable_notebook()
LDAvis_data_filepath = os.path.join('./results/ldavis_prepared_'+str(num_topics))
# # this is a bit time consuming - make the if statement True
# # if you want to execute visualization prep yourself
if 1 == 1:
    LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)
# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)
pyLDAvis.save_html(LDAvis_prepared, './results/ldavis_prepared_'+ str(num_topics) +'.html')
LDAvis_prepared