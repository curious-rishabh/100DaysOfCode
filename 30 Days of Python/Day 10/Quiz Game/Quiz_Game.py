# Quiz Game using OOP
# Day 10 of 100DaysOfCode
from data import question_data
import random
from quiz_brain import QuizBrain

class Question:
    def __init__(self,q_text ,q_answer):
        self.question = q_text
        self.answer = q_answer


question_bank = []
# Adding data to list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_que()


print("You have completed th quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")