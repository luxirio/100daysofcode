from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

api_params = {
    "amount":10,
    "type":"boolean"
}
quiz_request = requests.get("https://opentdb.com/api.php", api_params)
data = quiz_request.json()['results']

# Taking the data results and appending into the question_bank list
question_bank = []

# Generating the list
for question in data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the program
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# Finalizing the program
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
