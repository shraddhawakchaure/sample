# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:00:30 2021

@author: sheet
"""

import sqlite3
import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
from tkinter.filedialog import askopenfilename
import os
import cv2


window = tk.Tk()
window.geometry("700x700")
window.title("REGISTRATION FORM")
window.configure(background="grey")
global file
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
photo=tk.StringVar()
#file=tk.StringVar()
file1=tk.StringVar()

rollno = tk.StringVar()

value = random.randint(1, 1000)
print(value)

sqliteConnection = sqlite3.connect('evaluation.db')
cursor = sqliteConnection.cursor()
print("Connected to SQLite")
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(roll_no TEXT,Fullname TEXT,address TEXT,Email TEXT,Phoneno TEXT,Gender TEXT,age TEXT,photo BLOB NOT NULL)")

sqliteConnection.commit()


def show():
    global file
    file = askopenfilename(initialdir=r'D:\online_exam\profile images', title='Select Image',
                                       filetypes=[("all files", "*.*")])
    
    image3 =Image.open(file)
    image3 =image3.resize((450,280), Image.Resampling.LANCZOS)
    print(file)
    return file


def convertToBinaryData(filename):             #We have to add image to database thats why use this function to convert image into binary format
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB():
    global file
    fname = Fullname.get()
    addr = address.get()
    #un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    photo1 = file
    #Photo = convertToBinaryData(photo1)
    print(photo1)
   
    Reg = rollno.get()
    try:
        sqliteConnection = sqlite3.connect('evaluation.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_blob_query = """INSERT INTO registration
                                  (roll_no,Fullname,address,Email,Phoneno,Gender,age,photo) 
                                  VALUES(?,?,?,?,?,?,?,?)"""

        empPhoto = convertToBinaryData(photo1)
        #resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (Reg,fname, addr,email,mobile,gender,time,empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
    ms.showinfo("Student Record","Student Registration Completed !!")
    window.destroy()

image2 = Image.open('bg1.jpg')
image2 = image2.resize((700, 700), Image.Resampling.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="#192841", fg="white")
l1.place(x=190, y=50)


# that is for label1 registration

l10 = tk.Label(window, text="Roll No.", width=13, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=130, y=150)

t10 = tk.Entry(window, textvar=rollno, width=20, font=('', 15))
t10.place(x=330, y=150)

l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=130, y=200)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=200)
# that is for label 2 (full name)


l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=130, y=250)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=330, y=250)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=130, y=300)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=330, y=300)
# that is for email address

l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=130, y=350)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=330, y=350)
# phone number
l7 = tk.Label(window, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=130, y=400)
# gender
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value=1).place(x=330,
                                                                                                                y=400)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value=2).place(
    x=440, y=400)

l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=130, y=450)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=330, y=450)

l4 = tk.Button(window, text="Upload Photo", width=12, font=("Times new roman", 15, "bold"), bg="snow",command=show)
l4.place(x=230, y=500)
#file1=show(file)
#t3 = tk.Entry(window, textvar=file1, width=20, font=('', 15))
#t3.place(x=330, y=450)




btn = tk.Button(window, text="Register", bg="#192841",font=("",20),fg="white", width=9, height=1, command=insertBLOB)
btn.place(x=260, y=600)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()