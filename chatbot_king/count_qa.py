from konlpy.tag import Mecab
from collections import defaultdict
from definition import *

class count_answer:

    def __init__(self):
        self.mecab = Mecab()
        self.dic = self.make_pos_dic()

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

    def count_dic(self, phrase):
        dic = defaultdict(int)
        tags = self.mecab.pos(phrase)
        for word, pos in tags:
            if pos in NOUN:
                if word == '무엇':
                    dic[(word, pos)] = WHAT_WEIGHT
                else:
                    dic[(word, pos)] = NOUN_WEIGHT

            elif pos.count(VERB[0]): # VV + ETM.. 등이 존재하므로
                dic[(word, pos)] = VERB_WEIGHT

            elif pos in JOSA:
                dic[(word, pos)] = JOSA_WEIGHT

            else:
                dic[(word, pos)] = 1

        return dic

    def make_pos_dic(self, input_path='./data/training_data.txt'):
        dic = []
        with open(input_path, encoding='cp949') as f:
            lines = f.readlines()
            for line in lines:
                line = line.split('\t')
                dic.append((line[1].replace('\n', ''), self.count_dic(self.pre_phrase(line[0]))))

        return dic

    def multi_infer(self, phrase):
        phrase = self.pre_phrase(phrase)
        target = set(self.mecab.pos(phrase))
        count = 0
        index = []
        for i, refers in self.dic:
            temp = 0
            for word in target:
                if word in refers.keys():
                    temp += refers[word]

            # Todo: normalization
            # temp = temp * len(target) / len(refers)
            # if len(refers) - len(target) > 5:
            #     temp -= 5

            if temp > count:
                index = [i]
                count, temp = temp, count
            elif temp == count:
                index.append(i)
                count, temp = temp, count

        # if int(label) != int(index[-1][0]):
        #     print(index, label, target, dic[index[-1][0]])
        # print(index[-1][0][:2])
        return index

    def infer(self, phrase):
        return self.multi_infer(phrase)[-1]

    def infer_file(self, test_path = './data/training_data.txt'):
        with open(test_path, encoding='cp949') as f:
            lines = f.readlines()
            for line in lines[:]:
                tmp = line.split(',')
                sentence =self.pre_phrase(tmp[0])
                print(self.infer(sentence))


                # print('추론 : ', self.infer(sentence), '정답 : ', label)


# a = count_answer()
# print(a.dic)
# print(a.infer('진흥왕의 성은?'))