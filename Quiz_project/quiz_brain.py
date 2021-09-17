question_nos= 0
question_list = []
score = 0

class QuizBrain:
    def __init__(self, q_list):
        self.question_nos = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_nos < len(self.question_list)
            
    def next_question(self):
        current_question = self.question_list[self.question_nos]
        self.question_nos += 1
        user_answer=input(f"Q.{self.question_nos}: {current_question.question}(True/False):")
        self.check_answer(user_answer, current_question.correct_answer)
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1 
            print("right")
            print(f"The correct answer was; {correct_answer}")
            print(f"Your correct Score is; {self.score}/{self.question_nos}")
        else:
            print("wrong")
            print(f"The correct answer was; {correct_answer}")
            print(f"Your correct Score is; {self.score}/{self.question_nos}")
  



