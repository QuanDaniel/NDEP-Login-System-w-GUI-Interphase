#import modules
from tkinter import *
from tkinter import ttk
import os
import Dictionary as dc
import time
import sys


#TimeFunctions
def slow_print(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)


def slow_input(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
    user_input = input()


# Design window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x320")
    register_screen.configure(bg="brown")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please register below").pack()

    Label(register_screen, bg="brown", text="").pack()
    username_label = Label(register_screen, text="Username").pack()

    Label(register_screen, bg="brown", text="").pack()
    username_entry = Entry(register_screen, textvariable=username)

    username_entry.pack()

    Label(register_screen, bg="brown", text="").pack()
    password_label = Label(register_screen, text="Password").pack()

    Label(register_screen, bg="brown", text="").pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, bg="brown", text="").pack()

    Button(register_screen,
           text="Register",
           width=10,
           height=1,
           command=register_user).pack()


#Design window for scanner
def scanner():
    global scanner_screen
    scanner_screen = Toplevel(main_screen)
    scanner_screen.title("Scanner")
    scanner_screen.geometry("300x310")
    scanner_screen.configure(bg="brown")

    Label(scanner_screen, bg="brown", text="").pack()
    Label(scanner_screen, bg="brown", text="").pack()
    Label(scanner_screen, bg="brown", text="").pack()
    Label(scanner_screen, text="Choose Recon Method").pack()
    Label(scanner_screen, bg="brown", text="").pack()
    Button(scanner_screen,
           text="Username Finder",
           width=12,
           height=2,
           bg="lime green",
           command=usernamefinder).pack()
    Label(scanner_screen, bg="brown", text="").pack()

    Button(scanner_screen,
           text="Username Verify",
           width=12,
           height=2,
           bg="purple",
           command=usernameverify).pack()

#Design window for attack screen
def attack():
    global attack_screen
    attack_screen = Toplevel(main_screen)
    attack_screen.title("Attack")
    attack_screen.geometry("300x310")
    attack_screen.configure(bg="brown")

    #Set label for user instructions
    Label(attack_screen, bg="brown", text="").pack()
    Label(attack_screen, bg="brown", text="").pack()
    Label(attack_screen, bg="brown", text="").pack()
    Label(attack_screen, text="Choose Attack Method").pack()
    Label(attack_screen, bg="brown", text="").pack()

    #BruteForce Button
    Button(attack_screen,
           text="Brute Force",
           width=12,
           height=2,
           bg="turquoise",
           command=bruteforce).pack()
    Label(attack_screen, bg="brown", text="").pack()

    #Dictionary Button
    Button(attack_screen,
           text="Dictionary",
           width=12,
           height=2,
           bg="yellow",
           command=dictionaryattack).pack()
    Label(attack_screen, bg="brown", text="").pack()


# Designing window for login
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x310")
    login_screen.configure(bg="Brown")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, bg="brown", text="").pack()
    Label(login_screen, bg="brown", text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username").pack()
    Label(login_screen, bg="brown", text="").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, bg="brown", text="").pack()
    Label(login_screen, text="Password").pack()
    Label(login_screen, bg="brown", text="").pack()
    password_login_entry = Entry(login_screen,
                                 textvariable=password_verify,
                                 show='*')
    password_login_entry.pack()
    Label(login_screen, bg="brown", text="").pack()
    Button(login_screen,
           text="Login",
           width=10,
           height=1,
           command=login_verify).pack()


# Implement event on register button
def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen,
          text="Registration Success",
          fg="green",
          font=("calibri", 11)).pack()


#Implement event on username finder
def usernamefinder():
    slow_print("SCANNING FILES IN DATABASE")
    print(" ")
    time.sleep(5)
    for username in os.listdir():
        print(username)
    print(" ")

#Implement event on username verify 
def usernameverify():
    verification = input("Enter username for database verification: ")
    print("")
    slow_print("VERIFYING USER EXISTENCE")
    time.sleep(5)
    if verification in os.listdir():
        print(" ")
        slow_print("USER EXISTS")
        print(" ")
    else:
        slow_print("USER NOT FOUND")
        print(" ")


#Implement event on Dictionary button
def dictionaryattack():
    global getpw
    found = False
    slow_print("DICTIONARY ATTACK:")
    print(" ")
    userinput = input("ENTER USERNAME: ")
    print(" ")
    if userinput in os.listdir():
        slow_print("ACCESS GRANTED:")
        print(" ")
        openfile = open(userinput, "r")
        getpw = openfile.read().splitlines()
    else:
        slow_print("ACCESS DENIED:")
        print(" ")
        slow_print("USER NOT FOUND")
        print(" ")
    count = 0
    for password in dc.dict1:
        count += 1
        start = time.time()
        if userinput in os.listdir():
            if getpw[1] == password:
                time.sleep(1)
                slow_print("USER: " + userinput + " " + "PASSWORD:" + password)
                print(" ")
                found = True
                end = time.time()
                dictime = end - start
                print("Dictionary attack took", dictime,
                      "seconds to crack password after", count, "tries")
                print(" ")
                break
    if not found and userinput in os.listdir():
        time.sleep(5)
        slow_print("PASSWORD NOT FOUND")
        print(" ")


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


# Bruteforce Algorithm to search for a password by finding all combinations of a string with repetition
def bruteforce():
    found1 = False
    the_character_set = "abcdefghijklmnopqrstuvwxyz"
    the_character_set = the_character_set + "9876543210"
    the_character_set = the_character_set + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    the_character_set = the_character_set + "!()-.?[]_`~;:!@#$%^&*+="
    slow_print("BRUTE FORCE ATTACK:")
    print(" ")
    bruteuser = input("ENTER USERNAME: ")
    print(" ")
    for user in os.listdir():
        if user == bruteuser:
            slow_print("ACCESS GRANTED: ")
            print(" ")
            openfile1 = open(bruteuser, "r")
            split_file = openfile1.read().splitlines()
            the_password = split_file[1]
            the_password_length = len(the_password)
            final_list = [[]]
            tries = 0
            start = time.time()
            the_time = start
            groups = [list(the_character_set)] * the_password_length
            for i in groups:
                final_list = [x + [y] for x in final_list for y in i]
                guessed_passwords = [''.join(item) for item in final_list
                                     ]  #   all possible passwords
#checking for a particular password
            for guessed_password in guessed_passwords:
                tries += 1
                if guessed_password == the_password:
                    slow_print("PASSWORD MATCH")
                    print(" ")
                    slow_print("USER:" + bruteuser + " " + "PASSWORD:" +
                               guessed_password)
                    print(" ")
                    found1 = True
                    end = time.time()
                    the_time = end - start
                    print("Brute Force took", the_time,
                          "seconds to crack password after", tries, "tries")
                    print(" ")
                    break
    if not found1:
      slow_print("USER NOT FOUND")
      print(" ")


# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()


# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen,
           text="OK",
           command=delete_password_not_recognised).pack()


# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen,
           text="OK",
           command=delete_user_not_found_screen).pack()


# Deleting popups
def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x320")
    main_screen.title("OPERATION PASSWORD")
    main_screen.configure(bg="brown")
    Label(text="OPERATION PASSWORD",
          bg="brown",
          width="300",
          height="2",
          font=("Calibri", 13)).pack()
    Label(bg="brown", text="").pack()
    Button(text="Register",
           bg="blue",
           height="2",
           width="30",
           command=register).pack()
    Label(bg="brown", text="").pack()
    Button(text="Login", bg="green", height="2", width="30",
           command=login).pack()
    Label(bg="brown", text="").pack()
    Button(text="Scanner",
           bg="orange",
           height="2",
           width="30",
           command=scanner).pack()
    Label(bg="brown", text="").pack()
    Button(text="Attack", bg="Red", height="2", width="30",
           command=attack).pack()
    main_screen.mainloop()


main_account_screen()
