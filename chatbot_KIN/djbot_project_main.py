from count_qa import count_answer
from ebd_qa import embd_answer
from df_qa import dialogflow_answer
import getpass

print('start')
user_name = getpass.getuser()
student_Number = input('Student Number: ')
student_Name = input('Student Name: ')

# 절대 경로 설정

# 3CF0-499D

abspath = str(user_name)
abspath_QUERY = '/media/' + abspath + '/3CF0-499D/CT4302_query.txt'
abspath_ANSWER = '/media/' + abspath + '/3CF0-499D/CT4302_answer.txt'
abspath_RESPONE = '/media/' + abspath + '/3CF0-499D/CT4302_' + student_Number + '_' + student_Name + '.txt'

# abspath = '/home/' + str(user_name)
# abspath_QUERY = abspath + '/바탕화면/' + 'CT4302_query.txt'
# abspath_ANSWER = abspath + '/바탕화면/' + 'CT4302_answer.txt'
# abspath_RESPONE = abspath + '/바탕화면/' + 'CT4302_' + student_Number + '_' + student_Name + '.txt'

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

def sendTalk(text):
    DQ = dialogflow_answer()
    CQ = count_answer()
    EQ = embd_answer()
    if len(text) < 6:
        print('응답결과: ', 0)
        speech = 0
        response_log = open(abspath_RESPONE, 'a')
        response_log.write(str(speech) + '\n')
        response_log.close()
        return
    try:
        speech = answer(DQ.infer(text), CQ.multi_infer(text), EQ.infer(text))
    except:
        speech = 0

    print("응답결과: ", speech)
    response_log = open(abspath_RESPONE, 'a')
    response_log.write(str(speech) + '\n')
    response_log.close()


if __name__ == '__main__':

    database_set = 0
    number = 0

    total_trainingSET = 80
    total_developmentSET = 100
    total_testSET = 300

    # training_scoring =TS
    TS_answer = 0
    TS_ood = 0
    TS_fail = 0

    # development_scoring =DS
    DS_answer = 0
    DS_ood = 0
    DS_fail = 0

    # test_scoring = TES
    TES_answer = 0
    TES_ood = 0
    TES_fail = 0

    query_log = open(abspath_QUERY, 'r')
    query_lines = query_log.readlines()
    len_QUERY = len(query_lines)


    print ('[CT4302] Project #1 Q&A Chatbot Competition \n')
    print ('총 질문 개수: ' + str(len_QUERY) + '\n')

    for query in query_lines:
        sendTalk(str(query))

    query_log.close()

    log_RESPONSE = open(abspath_RESPONE, 'r')
    log_ANSWER = open(abspath_ANSWER, 'r')

    lines_RESPONSE = log_RESPONSE.readlines()
    lines_ANSWER = log_ANSWER.readlines()
    lines_NUMBER = len(lines_RESPONSE)

    for number in range(0, 80):
        #############################################################
        if int(lines_RESPONSE[number]) == int(lines_ANSWER[number]):
            TS_answer += 1
        else:
            TS_fail += 1

    for number in range(80, 180):
        #############################################################
        if int(lines_RESPONSE[number]) == int(lines_ANSWER[number]):
            DS_answer += 1
        else:
            DS_fail += 1

    for number in range(180, 480):
        #############################################################
        if int(lines_RESPONSE[number]) == int(lines_ANSWER[number]):
            TES_answer += 1
        else:
            TES_fail += 1

    log_RESPONSE.close()
    log_ANSWER.close()

    TS_scoring = 0.2 * (float(TS_answer) / float(total_trainingSET))
    DS_scoring = 0.3 * (float(DS_answer) / float(total_developmentSET))
    TES_scoring = 0.5 * (float(TES_answer) / float(total_testSET))

    finial_scroing = 100 * (TS_scoring + DS_scoring + TES_scoring)

    print("\n")
    print("총 질문 수: " + str(lines_NUMBER) + "\n")

    print('< Training Set 80 >')
    print("총 Training 정답 수: " + str(TS_answer))
    print("총 Training 틀린 수: " + str(TS_fail))
    print("총 Training 점수: " + str(TS_scoring) + "\n")

    print('< Development Set 100 >')
    print("총 Development 정답 수: " + str(DS_answer))
    # print("총 Development OOD 수: " + str(DS_ood))
    print("총 Development 틀린 수: " + str(DS_fail))
    print("총 Development 점수: " + str(DS_scoring) + "\n")

    print('< Test Set 300 >')
    print("총 Test 정답 수: " + str(TES_answer))
    # print("총 Test OOD 수: " + str(TES_ood))
    print("총 Test 틀린 수: " + str(TES_fail))
    print("총 Test 점수: " + str(TES_scoring) + "\n")

    print("총 점수: " + str(finial_scroing))
