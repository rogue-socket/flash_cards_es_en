import pandas as pd
import tkinter as tk
import random
from tkinter import messagebox

# ---------------------------- WORD GENERATION AND LOGIC ----------------------------

csv_data = pd.read_csv("es_en_words.csv")
en_words = list(csv_data.en_words)
es_words = list(csv_data.es_words)
known_words_list_es = []
known_words_list_en = []
current_en_word = None
current_es_word = None


def know():
    global known_words_list_en
    global known_words_list_es
    known_words_list_es.append(current_es_word)
    known_words_list_en.append(current_en_word)
    es_words.remove(current_es_word)
    en_words.remove(current_en_word)
    print(known_words_list_en)
    call_word()


def unknown():
    call_word()


def call_word():
    index = random.randint(0, len(es_words))
    global current_es_word
    global current_en_word
    es_word = es_words[index]
    en_word = en_words[index]
    current_en_word = en_word
    current_es_word = es_word
    normal_card(es_word)
    # wait for 3 seconds
    window.after(500, flip_card, en_word)


# ---------------------------- COUNT-DOWN MECHANISM ----------------------------

def flip_card(en_word_show):
    # Will show the back of the card
    canvas.create_image(400, 300, image=back_image)
    canvas.create_text(400, 250, text=en_word_show, fill="white", font=("Helvetica", 35, "bold"))
    canvas.create_text(400, 450, text="English", fill="white", font=("Helvetica", 20, "bold"))
    # esp_word_card = canvas.create_text(200, 150, text=en_word_show, fill="white")


def normal_card(es_word_show):
    canvas.create_image(400, 300, image=front_image)
    canvas.create_text(400, 250, text=es_word_show, fill="black", font=("Helvetica", 35, "bold"))
    canvas.create_text(400, 450, text="Spanish", fill="black", font=("Helvetica", 20, "bold"))


# ---------------------------- UI ----------------------------
window = tk.Tk()
window.title("Flash Cards")
window.minsize(width=900, height=630)
window.config(bg="#B1DDC6", padx=50, pady=15)

canvas = tk.Canvas(width=800, height=600, highlightthickness=0)
front_image = tk.PhotoImage(file="card_front.png")
back_image = tk.PhotoImage(file="card_back.png")
canvas.create_image(400, 300, image=front_image)

canvas.create_text(400, 260, text="Welcome to Spanish -> English", fill="black", font=("Helvetica", 30, "bold"))
canvas.create_text(400, 320, text="flashcards", fill="black", font=("Helvetica", 30, "bold"))

canvas.config(bg="#B1DDC6")
canvas.grid(row=0, column=0, columnspan=2)

right_image = tk.PhotoImage(file="right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, borderwidth=0, relief="flat", command=know)
right_button.grid(row=1, column=1)

wrong_image = tk.PhotoImage(file="wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, borderwidth=0, relief="flat", command=unknown)
wrong_button.grid(row=1, column=0)

resp = messagebox.askyesno("Ready?", "Are you ready?")

if resp:
    window.after(1000, call_word)
else:
    resp = messagebox.askyesno("Waiting...", "Click yes when you are ready")
    if resp:
        window.after(1000, call_word)
    else:
        exit()

window.mainloop()
