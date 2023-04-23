from tkinter import *

def create_window(window):
    window.geometry("450x300")
    window.config(bg="#21089B")
    window.title("Registration")

def labels(window):
    Label(window, text="Registration Form", font=("Calleo 25 bold"), fg="#A39CC6", bg="#21089B").grid(row=0, column=3)
    Label(window, text="Name", font=("Calleo 15 bold"), fg="#A39CC6", bg="#21089B").grid(row=1, column=2)
    Label(window, text="email", font=("Calleo 15 bold"), fg="#A39CC6", bg="#21089B").grid(row=2, column=2)
    Label(window, text="Phone", font=("Calleo 15 bold"), fg="#A39CC6", bg="#21089B").grid(row=3, column=2)
    Label(window, text="Password", font=("Calleo 15 bold"), fg="#A39CC6", bg="#21089B").grid(row=4, column=2)

def enter_uset_data(window, name_value=None, email_value=None, phone_value=None, password_value=None):
    Entry(window, textvariable = name_value, font=("Calleo 10 bold")).grid(row=1, column=3)
    Entry(window, textvariable = email_value, font=("Calleo 10 bold")).grid(row=2, column=3)
    Entry(window, textvariable = phone_value, font=("Calleo 10 bold")).grid(row=3, column=3)
    Entry(window, textvariable = password_value, show="*", font=("Calleo 10 bold")).grid(row=4, column=3)
    Label(window, text="", bg="#21089B").grid(row=5, column=3) # A blank line makes it to separate the button from the entry screen

    return {"name": name_value, "email": email_value, "phone": phone_value, "password": password_value}