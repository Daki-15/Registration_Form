# import the necessary modules and functions
from tkinter import *
from tkinter import messagebox
from design import create_window, labels, enter_uset_data

# creates the main window of the GUI.
window = Tk()
# create StringVar objects to hold the values entered by the user.
name_value = StringVar()
email_value = StringVar()
phone_value = StringVar()
password_value = StringVar()

# call the create_window and labels functions to create the GUI.
create_window(window)
labels(window)

# calls the enter_user_data function to create entry fields for the user to enter their information
user_data = enter_uset_data(window, name_value, email_value, phone_value, password_value)

# checks if all the entry fields are filled or not
def get_values():
    if ( user_data['name'].get() == ""):
        messagebox.showerror("Error", "You forgot to write your name")
    elif ( user_data['email'].get() == ""):
        messagebox.showerror("Error", "You forgot to write your email")
    elif ( user_data['phone'].get() == ""):
        messagebox.showerror("Error", "You forgot to write your phone")
    elif ( user_data['password'].get() == ""):
        messagebox.showerror("Error", "You forgot to write your password")
    else:
        print(f"[\n{user_data['name'].get()}, {user_data['email'].get()}, {user_data['phone'].get()}, {user_data['password'].get()}\n]")

# creates a Submit button and assigns the get_values function to it
Button(text="Submit", command = get_values, font=("Calleo 15 bold"), bg="#7474BD").grid(row=6, column=3)

#  starts the main event loop
window.mainloop()