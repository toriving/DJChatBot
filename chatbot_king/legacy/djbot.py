from count_qa import count_answer
from ebd_qa import embd_answer
from df_qa import dialogflow_answer

def answer(DA, CA, EA):
    DA = DA
    EA = EA

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

def QA():
    DQ = dialogflow_answer()
    CQ = count_answer()
    EQ = embd_answer()
    while True:
        str = input('Q : ')
        if len(str) == 0 or str == 'exit':
            print("종료합니다.")
            break
        elif len(str) < 5:
            print('정답 : 0')
            continue
        try:
            print("DQ :", DQ.infer(str), "CQ :", CQ.multi_infer(str), "EQ :", EQ.infer(str))
            print("정답 :", answer(DQ.infer(str), CQ.multi_infer(str), EQ.infer(str)))
        except:
            print('올바른 문장을 입력해주세요.')

def doc_QA():
    DQ = dialogflow_answer()
    CQ = count_answer()
    EQ = embd_answer()
    CQ.infer_file()
    print('----------------------------------------')
    EQ.infer_file()
    print('----------------------------------------')
    DQ.infer_file()

if __name__ == '__main__':
    QA()
    # doc_QA()
