from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: ", bg=THEME_COLOR, foreground="white", font=("Arial", 15, "bold"),
                                 highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text="00:00", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        correct_photo = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=correct_photo, highlightthickness=0, command=self.true_anwser)
        self.correct_button.grid(column=0, row=2)

        wrong_photo = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_photo, highlightthickness=0, command=self.false_anwser)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="NO MORE QUESTIONS")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_anwser(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_anwser(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

