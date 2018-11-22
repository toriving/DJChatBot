if __name__ == '__main__':

    # Scoring Test
    database_set = 0
    number = 0

    training_scoring_answer = 0
    training_scoring_ood = 0
    training_scoring_fail = 0

    development_scoring_answer = 0
    development_scoring_ood = 0
    development_scoring_fail = 0

    test_scoring_answer = 0
    test_scoring_ood = 0
    test_scoring_fail = 0

    query_log = open(abspath_QUERY, 'r')
    query_lines = query_log.readlines()
    len_QUERY = len(query_lines)

    print ('[CT4302] Project #1 Q&A Chatbot Competition \n')
    print ('총 질문 개수: ' + str(len_QUERY) + '\n')

    for database_set in query_lines:
            sendTalk(str(database_set))
    query_log.close()

    log_RESPONSE = open(abspath_RESPONE, 'r')
    log_ANSWER = open(abspath_ANSWER, 'r')

    lines_RESPONSE = log_RESPONSE.readlines()
    lines_ANSWER = log_ANSWER.readlines()
    lines_NUMBER = len(lines_RESPONSE)

    for number in range(0, 10):
        if lines_RESPONSE[number] == lines_ANSWER[number]:
            training_scoring_answer += 1
        elif number == '0':
            training_scoring_ood += 1
        else:
            training_scoring_fail += 1

    for number in range(10, 40):
        if lines_RESPONSE[number] == lines_ANSWER[number]:
            development_scoring_answer += 1
        elif number == '0':
            development_scoring_ood += 1
        else:
            development_scoring_fail += 1

    for number in range(40, 80):
        if lines_RESPONSE[number] == lines_ANSWER[number]:
            test_scoring_answer += 1
        elif number == '0':
            test_scoring_ood += 1
        else:
            test_scoring_fail += 1

    log_RESPONSE.close()
    log_ANSWER.close()
    finial_scroing = 0.2*training_scoring_answer + 0.3*development_scoring_answer + 0.5*test_scoring_answer

    print("\n")
    print("총 질문 수: " + str(lines_NUMBER))

    print ('Training Set 10')
    print("총 Training 정답 수: " + str(training_scoring_answer))
    print("총 Training OOD 수: " + str(training_scoring_ood))
    print("총 Training 틀린 수: " + str(training_scoring_fail) + "\n")

    print ('Development Set 30')
    print("총 Development 정답 수: " + str(development_scoring_answer))
    print("총 Development OOD 수: " + str(development_scoring_ood))
    print("총 Development 틀린 수: " + str(development_scoring_fail) + "\n")

    print ('Test Set 40')
    print("총 Test 정답 수: " + str(test_scoring_answer))
    print("총 Test OOD 수: " + str(test_scoring_ood))
    print("총 Test 틀린 수: " + str(test_scoring_fail) + "\n")

    print("총 점수: " + str(finial_scroing))