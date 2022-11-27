from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import pymysql

windows = Tk()
windows.geometry('500x460+200+10')
# windows.resizable(False,False)
windows.attributes('-transparentcolor', 'red')
windows.title('Simple Coding Style')

def back():
    windows.destroy()
    import loginpg

def submit():
     if usernameEntry.get() == '' or emailEntry.get() == '' or NewpasswordEntry.get() == '' or confirmpasswordEntry.get() == '':
         messagebox.showerror('Error', "Entry fields must be entered")
         return

     elif NewpasswordEntry.get() != confirmpasswordEntry.get():
         messagebox.showerror('Error', "Passwords don't match")
         return
     else:
         db = pymysql.connect(host='localhost', user='root', password='1234', database='p_registration')
         mycursor = db.cursor()
         query = 'select * from personaldata where email=%s'
         mycursor.execute(query, (emailEntry.get()))
         role=mycursor.fetchone() #to fetch the existing data
         if role==None: #if the data doesn't exit in the datababse then error message displays
             messagebox.showerror('Error', 'Incorrect email or password')
         else:
             query='update personaldata set passwrd=%s where email=%s' #this is the line of code to query the databse
             mycursor.execute(query, (NewpasswordEntry.get(),emailEntry.get()))
             db.commit() #to commit teh changes
             db.close() #then close after changes have been done
             messagebox.showinfo('Success', 'Succesful Changes please login with New password')

             windows.destroy()

             import loginpg


frame=Frame(windows, width=540, height=640, bg='black', bd=8)
frame.place(x=0,y=0)

#labels on window
heading =Label(frame, text='FORGOT PASSWORD', fg='#97FFFF', bg='black', font=('Calibre', 20, 'bold'))
heading.place(x=110, y=3)

usernameImage=PhotoImage(file='padlock.png')
usernameLabel=Label(frame, image=usernameImage)
usernameLabel.place(x=45, y=3)

usernamelbl = Label(frame, text='Username:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
usernamelbl.place(x=10, y=150)

usernameEntry=Entry(frame, width=30, borderwidth=2)
usernameEntry.place(x=250, y=150)

emaillbl = Label(frame, text='Email:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
emaillbl.place(x=10, y=200)

emailEntry=Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=250, y=200)

Newpasswordlbl = Label(frame, text='New Password:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
Newpasswordlbl.place(x=10, y=250)

NewpasswordEntry=Entry(frame, width=30, borderwidth=2)
NewpasswordEntry.place(x=250, y=250)

confirmPasswordlbl = Label(frame, text='Confirm New Password:', fg='#97FFFF', bg='black', font=('Calibre', 15, 'bold'))
confirmPasswordlbl.place(x=10, y=300)

confirmpasswordEntry=Entry(frame, width=30, borderwidth=2)
confirmpasswordEntry.place(x=250, y=300)

bckbtn = Button(frame, text='<<', width=7, borderwidth=5, height=2, bg='black', fg='white', cursor='hand2', border=2,
                command=back)
bckbtn.place(x=10, y=400)

submit1btn = Button(frame, text='Submit', width=15, height=2, bg='#7f7fff',fg='white', cursor='hand2', border=2, borderwidth=5, font=('#57a1f8', 16, 'bold'), command=submit)
submit1btn.place(x=130, y=350)

windows.mainloop()