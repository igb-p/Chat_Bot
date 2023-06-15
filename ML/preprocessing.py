import nltk
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
nltk.download("stopwords")
mystem = Mystem()
stopwords = stopwords.words("russian")

# стемминг, лемматизация, исключение цифр
def text_preprocessing (text):
  text = str(text)
  tokens = mystem.lemmatize(text.lower())
  tokens = [token for token in tokens if token not in stopwords or token in ['себя', 'себе'] \
   and token!=" " \
   and token.strip() not in punctuation\
   and token.isdigit()==False]
  text = " ".join(tokens)
  return text
