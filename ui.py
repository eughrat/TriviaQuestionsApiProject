from tkinter import *

THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: ", bg=THEME_COLOR, foreground="white", font=("Arial", 15, "bold"),
                                 highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text="00:00", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        correct_photo = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=correct_photo, highlightthickness=0)
        self.correct_button.grid(column=0, row=2)

        wrong_photo = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_photo, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        self.window.mainloop()
