from gensim.models import FastText
from konlpy.tag import Mecab
from sklearn.metrics.pairwise import cosine_similarity
from definition import *
import numpy as np

class embd_answer:

    def __init__(self):
        self.mecab = Mecab()
        self.load_data()

    def pre_phrase(self, phrase):
        for how in HOW:
            phrase = phrase.replace(how, HOW_TOKEN)
        for why in WHY:
            phrase = phrase.replace(why, WHY_TOKEN)
        for year in YEAR:
            phrase = phrase.replace(year, YEAR_TOKEN)
        for country in COUNTRY:
            phrase = phrase.replace(country, COUNTRY_TOKEN)
        for d in DEL:
            phrase = phrase.replace(d, '')
        return phrase


    def load_data(self):
        self.sentence = []
        with open('./data/training_data.txt', encoding='cp949') as f:
            lines = f.readlines()
            for line in lines:
                line = line.split('\t')
                line[0] = self.pre_phrase(line[0])
                self.sentence.append((line[1].replace('\n',''), self.mecab.morphs(line[0].replace('\n',''))))
        # training_set = [x[1] for x in self.sentence]
        # self.model1 = FastText(training_set, size=32, window=5, min_count=1, iter=10000, workers = 8)
        # self.model1.save('./data/model')
        # print('training finish')
        self.model = FastText.load('./data/model')

        self.l = []
        for index, word in self.sentence:
            avg = 0
            for j in word:
                avg += self.model[j]
            avg = avg / len(word)
            self.l.append((index, avg))

    def infer(self, phrase):
        phrase = self.pre_phrase(phrase)
        phrase = self.mecab.morphs(phrase)
        qv=0
        for i in phrase:
            try:
                qv += self.model[i]
            except:
                qv += np.zeros((32))
                pass

        qv = qv / len(phrase)

        max_ = 0
        index = 0
        for i, refer in self.l:
            tmp = cosine_similarity(refer.reshape(1,-1), qv.reshape(1,-1))
            if tmp > max_:
                max_ = tmp
                index = i

        # print(index + 1)
        return index

    def infer_file(self, path = './data/training_data.txt'):
        test = []
        with open(path, encoding='cp949') as f:
            lines = f.readlines()
            for line in lines:
                test.append(line.replace('\n',''))
        for q in test:
            print(self.infer(q))


# a = embd_answer()
# print(a.infer('신라의 한강유역 점령은 어떤 의미가 있나요?'))