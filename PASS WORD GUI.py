# importing the tkinter module
from tkinter import *
from subprocess import call

import os

# importing the pyperclip module to use it to copy our generated
# password to clipboard


# random module will be used in generating the random password
import random


# initializing the tkinter
root = Tk()

# setting the width and height of the gui
root.geometry("700x300")  # x is small case here

# declaring a variable of string type and this variable will be
# used to store the password generated
passstr = StringVar()

# declaring a variable of integer type which will be used to
# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)
def openStudentrecord():
    call(["python", "Studentrecord.py"])



# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate
    # the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']


    # declaring the empty string
    password = ""

    # loop to generate the random password of the length entered
    # by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)


# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)


# --------------------------------------------------------------------STUDENT LOGIN FORM--------------------------------------------------------------------
# Designing window for registration

def main_account_screen():
    global main_screen
    global login
    global register

    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")



def openRegister():
    global register_screen
    register_screen = Toplevel()
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    #password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()

    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()

    password_entry = Entry(register_screen, textvariable=passstr, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def openLogin():
    global login_screen
    login_screen = Toplevel()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

# Implementing event on register button


def register_user():
    username_info = username.get()
    password_info = passstr.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=openStudentrecord).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window


# Creating a text label widget
pass_label=Label(root, text="Password Generator Application", font="calibri 20 bold")
pass_label.grid(row=0, column=0, pady=3, padx=15, ipadx=2)

# Creating a text label widget
pass_len_label=Label(root, text="Enter password length")
pass_len_label.grid(row=1, column=0, pady=3, padx=15, ipadx=2)

# Creating a entry widget to take password length entered by the
# user
user_entry=Entry(root, textvariable=passlen)
user_entry.grid(row=2, column=0, pady=3, padx=15, ipadx=10)


# button to call the generate function
btn_pass=Button(root, text="Generate Password", command=generate)
btn_pass.grid(row=3, column=0, pady=3, padx=15, ipadx=10)


# entry widget to show the generated password
gen_pass=Entry(root, textvariable=passstr)
gen_pass.grid(row=4, column=0, pady=3, padx=15, ipadx=10)

# button to call the copytoclipboard function
btn_copy=Button(root, text="Copy to clipboard", command=copytoclipboard)
btn_copy.grid(row=5, column=0, pady=3, padx=15, ipadx=10)


btn_verify_register = Button(root, text="LOGIN", command=openLogin, fg="white", bg="green")
btn_verify_register.grid(row=6, column=0,padx=5, pady=5, ipadx=10)

btn_verify_login = Button(root, text="REGISTER", command=openRegister, fg="blue", bg="orange")
btn_verify_login.grid(row=6, column=1,padx=75,  pady=5, ipadx=8)

btn_verify_exit = Button(root, text="EXIT", command=root.quit, fg="white", bg="red")
btn_verify_exit.grid(row=7, column=5, padx=5, pady=5,  ipadx=15)




# mainloop() is an infinite loop used to run the application when
# it's in ready state
root.mainloop()
