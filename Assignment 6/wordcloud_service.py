from wordcloud import WordCloud
from matplotlib import pyplot as plt
import numpy

def create_worldcloud(data):
    final_text_str = data['final_text'].str.cat()

    spam_words = final_text_str = data.loc[data['label'] == 'spam']['final_text'].str.cat()

    wordcloud = WordCloud(background_color='white',
                                width=600,
                                height=400).generate(spam_words)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def create_bins(data):
    data['text_len'] = data['text'].apply(lambda x: len(x) - x.count(" "))

    bins = numpy.linspace(0, 250, 40)
    plt.hist(data['text_len'],bins)
    plt.title("text Length Distribution")
    plt.show()