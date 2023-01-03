'''
Text To Speech
-------------------------------------------------------------
pip install nltk newspaper3k gtts
'''

import nltk
from newspaper import Article
from gtts import gTTS


def text_to_speech(url):
   article = Article(url)
   article.download()
   article.parse()
   nltk.download('punkt')
   article.nlp()
   article_text = article.text
   language = 'en'
   my_obj = gTTS(text=article_text, lang=language, slow=False)
   my_obj.save("santosh_ghimire.mp3")


if __name__ == '__main__':
   text_to_speech(
       url='https://www.sharesansar.com/newsdetail/reminder-last-day-to-grab-dividend-of-shivm-mnbbl-hdl-5-other-companies-2023-01-03'
   )