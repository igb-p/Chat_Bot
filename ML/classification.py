import pickle
import pandas as pd
from preprocessing import text_preprocessing


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline


# загрузка датасета из файла
data = {'Реплика':[], 'Категория':[]}
for line in open('dataset.txt'):
    doc_line = line.split('@')
    data['Реплика'].append(doc_line[0])
    data['Категория'].append(doc_line[1].strip())
df = pd.DataFrame(data)


x = df.Реплика
y = df.Категория
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10)
 
#vectorizer = CountVectorizer()

#обучение
text_clf = Pipeline([

('count', CountVectorizer(ngram_range=(1,2))), 
('clf', MultinomialNB())])

text_clf = text_clf.fit(x, y)
with open ('data.pickle', 'wb') as f:
    pickle.dump(text_clf, f )
