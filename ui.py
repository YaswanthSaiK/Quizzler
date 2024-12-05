from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.config(bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.Question = self.canvas.create_text(150, 120,
                                                text="some questions ",
                                                width=280,
                                                fill=THEME_COLOR,
                                                font=("ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10, padx=10)

        self.score = Label(text="Score : 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, pady=10, padx=10)

        ri = PhotoImage(file='images/true.png')
        wi = PhotoImage(file='images/false.png')

        self.right = Button(image=ri, width=90, height=90, highlightthickness=0, command=self.rightl)
        self.right.grid(column=0, row=2, pady=10, padx=10)

        self.wrong = Button(image=wi, width=90, height=90, highlightthickness=0, command=self.wrongl)
        self.wrong.grid(column=1, row=2, pady=10, padx=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.Question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.Question, text="You have got to the end  of the quiz !!!!!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def rightl(self):
        self.give_feedback(self.quiz.check_answer('true'))
        # self.get_next_question()

    def wrongl(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
