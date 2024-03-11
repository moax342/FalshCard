from tkinter import *
import pandas
import random

BACKGROUND_COLOR: str = "#B1DDC6"
to_learn={}
current_card={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------- Functionality ----------- #
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    fr_lang="French"
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_background, image=CARD_FRONT)
    canvas.itemconfig(title_word,text=fr_lang,fill="black")
    canvas.itemconfig(the_word, text=current_card[fr_lang], fill="black")
    flip_timer=window.after(3000, func=flip_card)
def flip_card():
    global current_card
    en_lang="English"
    canvas.itemconfig(card_background,image=CARD_BACK)
    canvas.itemconfig(title_word,text=en_lang,fill="white")
    canvas.itemconfig(the_word, text=current_card[en_lang], fill="white")

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv",index=False)
    next_card()
    # ------- the UI for the project ------- #

window = Tk()

window.title("Learn From Fash")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

# --------- All images here ------------ #
CARD_FRONT = PhotoImage(file="images/card_front.png")
CARD_BACK = PhotoImage(file="images/card_back.png")
RIGHT_IMAGE = PhotoImage(file="images/right.png")
WRONG_IMAGE = PhotoImage(file="images/wrong.png")
# --------- All images ends here ------------ #

canvas = Canvas(width=800, height=526)
card_background=canvas.create_image(400,263,image=CARD_FRONT)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title_word = canvas.create_text(400, 200, text="", fill="black",
                             font=("Arial", 40, "italic"))
the_word= canvas.create_text(400, 290, text="", fill="black",
                             font=("Arial", 50, "bold"))
canvas.grid(row=0,column=1)
# --- buttons for the game ---- #
right_button=Button(image=RIGHT_IMAGE,width=100,height=100,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=2,)
wrong_button=Button(image=WRONG_IMAGE,width=100,height=100,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
# --- buttons END for the game ---- #
next_card()

window.mainloop()
