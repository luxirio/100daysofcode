from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz):
        self.quiz = quiz
        # Initial parameters
        self.window = Tk()
        self.window.title("Quizzler!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # Label (score)
        self.score = Label(text=f'Score: {quiz.score}', 
        bg=THEME_COLOR, 
        font=("Arial", 15, "bold"),
        padx=20, pady=20, fg="white")
        self.score.grid(row=0, column=1)
        
        # Generating canvas (where the question text is going to be)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.canvas_text = self.canvas.create_text(150,125, 
                                                    text=quiz.current_question, 
                                                    font=("Arial", 20), 
                                                    width=280)

        # Now the buttons
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, command=self.get_question)
        self.false_button.grid(row=2, column=0)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, command=self.get_question)
        self.true_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=q_text)
        