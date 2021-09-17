

from typing import Text


class Question():
    def __init__(self, q_category,q_question,q_difficulty,q_type, q_correct_answer,q_incorrect_answers):
        self.category = q_category
        self.question = q_question
        self.type = q_type
        self.dificulty = q_difficulty
        self.correct_answer = q_correct_answer
        self.incorrect_answers = q_incorrect_answers
       