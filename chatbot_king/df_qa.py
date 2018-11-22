import json
import apiai

class dialogflow_answer:

    def sendTalk(self, text):
        token = 'f6330705a27b4903be52ef8ad1145096'
        ai = apiai.ApiAI(token)
        request = ai.text_request()
        request.lang = 'ko'
        request.session_id = 'chat'
        request.query = text

        response = request.getresponse()

        if response.status == 200:
            try:
                response_structure = json.loads(response.read().decode('utf-8'))
                speech = response_structure['result']['fulfillment']['messages'][0]['speech']

                if speech is not None:
                    return speech
                else:
                    return
            except:
                return

    def infer(self, phrase):
        return self.sendTalk(phrase)


    def infer_file(self, test_path='./data/training_data.txt'):
        with open(test_path, encoding='cp949') as f:
            lines = f.readlines()
            for line in lines[:]:
                tmp = line.split(',')
                print(self.infer(tmp[0]))
