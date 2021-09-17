from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]

for question in question_data:
    new_question = Question(q_question = question["question"],q_correct_answer = question["correct_answer"], q_type = question['type'],q_category = question['category'],q_difficulty = question['difficulty'],q_incorrect_answers = question['incorrect_answers'])
    question_bank.append(new_question)

print(question_bank[0].correct_answer)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final Score is {quiz.score}/{quiz.question_nos}")
