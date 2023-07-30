from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question = questions["question"]
    answer = questions["correct_answer"]
    new_question = Question(text=question, answer=answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    try:
        quiz.next_question()
    except IndexError:
        break

print("There are no more questions. You've completed the quiz")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")
