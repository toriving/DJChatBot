from count_qa import count_answer
from ebd_qa import embd_answer
from df_qa import dialogflow_answer
import getpass

user_name = getpass.getuser()
student_Number = input('Student Number: ')
student_Name = input('Student Name: ')

# 절대 경로 설정
abspath = '/home/' + str(user_name)
abspath_QUERY = abspath + '/바탕화면/' + 'CT4302_query.txt'
abspath_ANSWER = abspath + '/바탕화면/' + 'CT4302_answer.txt'
abspath_RESPONE = abspath + '/바탕화면/' + 'CT4302_' + student_Number + '_' + student_Name + '.txt'

def answer(DA, CA, EA):
    DA = int(DA)
    EA = int(EA)
    # print(DA, CA, EA)
    if CA[-1] == 0 and DA != EA:
        return 0

    elif DA in CA:
        return DA

    elif DA not in CA:
        if DA == EA:
            return DA

        elif EA in CA:
            return EA

        else:
            return 0

    else:
        return 0

def QA(text):
    DQ = dialogflow_answer()
    CQ = count_answer()
    EQ = embd_answer()
    if len(text) < 5:
        print('응답결과: ', 0)
        speech = str(0)
        response_log = open(abspath_RESPONE, 'a')
        response_log.write(speech + '\n')
        response_log.close()
        return
    try:
        speech = answer(DQ.infer(text), CQ.multi_infer(text), EQ.infer(text))
    except:
        speech = str(0)

    print("응답결과: ", speech)
    response_log = open(abspath_RESPONE, 'a')
    response_log.write(str(speech) + '\n')
    response_log.close()


if __name__ == '__main__':
    # Scoring Test
    query = 0
    number = 0
    scoring = 0
    fail = 0

    query_log = open(abspath_QUERY, 'r')
    query_lines = query_log.readlines()
    len_QUERY = len(query_lines)

    print('[CT4302] Project #1 Q&A Chatbot Competition \n')
    print('총 질문 개수: ' + str(len_QUERY) + '\n')

    for query in query_lines:
        QA(str(query))

    query_log.close()

    log_RESPONSE = open(abspath_RESPONE, 'r')
    log_ANSWER = open(abspath_ANSWER, 'r')

    lines_RESPONSE = log_RESPONSE.readlines()
    lines_ANSWER = log_ANSWER.readlines()

    len_RESPONSE = len(lines_RESPONSE)

    for number in range(len_RESPONSE):
        if lines_RESPONSE[number] == lines_ANSWER[number]:
            scoring += 1
        else:
            fail += 1

    log_RESPONSE.close()
    log_ANSWER.close()

    print("\n")
    print("총 질문 수: " + str(len_RESPONSE))
    print("총 정답 수: " + str(scoring))
    print("총 틀린 수: " + str(fail))


