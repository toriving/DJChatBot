NOUN = ['NNG', 'NNP', 'NNB', 'NNBC', 'NR', 'NP']
NOUN_WEIGHT = 3

# 부사격조사는 제외 (에서, 으로, 에, ...) , 접속조사는 여러가지의 차이를 나타낼수 있으므로 제외 (와, 과, ..)
JOSA = ['JKS', 'JKC', 'JKG', 'JKO', 'JKV', 'JKQ', 'JX']
JOSA_WEIGHT = 0

VERB = ['VV']
VERB_WEIGHT = 2

WHAT = ['무엇', '것', '어떤'] # 1
WHAT_WEIGHT = 1

# WHO = ['누가']
#
# WHERE = ['어디서']

HOW = ['어떻게', '방법', '원리', '어떡', '법', '어째서']
HOW_TOKEN = '어떻'

WHY = ['왜', '이유', '원인', '까닭']
WHY_TOKEN = '왜'

DEL = ['인가요', '나요', '?']
