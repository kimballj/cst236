from pyTona.question_answer import QA
from pyTona.answer_funcs import feet_to_miles, hal_20

import difflib
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why"]
        self.question_mark = chr(0x3E)

        self.question_answers = {
            'What is feet in miles': QA('What is feed in miles', feet_to_miles),
            'How many seconds since': QA('How many seconds since', '42 seconds'),
            'Who invented Python': QA('Who invented Python', 'Guido Rossum(Benevolent Dictator For Life)'),
            'Why don\'t you understand me': QA('Why don\'t you understand me', 'Because you do not speak 1s and 0s'),
            'Why don\'t you shutdown': QA('Why don\'t you shutdown', hal_20)

        }
        self.last_question = None

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question.split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-2]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                print answer.question
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except:
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)