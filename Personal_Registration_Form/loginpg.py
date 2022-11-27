from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

windows=Tk()

windows.title('Simple Coding Style')
windows.geometry('490x240+200+200')
# windows.resizable(0,0)

#forgot password
def forgot_password():
    windows.destroy()
    import forgotpassword

#Button Definition process
def create_one():
    windows.destroy()
    import Registration2


def login():
    if idEntry.get()=='' or passwdEntry.get()=='': #if this condition is true it'll show an error box
        messagebox.showerror('Alert', 'Please enter all entry fields!')


    else:
        db = pymysql.connect(host='localhost', user='root', password='1234', database='p_registration')
        cur = db.cursor()
        query = 'select * from personaldata where passwrd=%s'
        cur.execute(query, (passwdEntry.get()))
        roles = cur.fetchone()


        if roles == None:
            messagebox.showerror('Alert!', 'Incorrect email or password')
            return


        else:
            messagebox.showinfo('success', 'Login Successful')
            #clear scree
            idEntry.delete(0, END)
            passwdEntry.delete(0, END)
            # windows.destroy()


#email
def on_entry(e):
    idEntry.delete(0, END)

def on_password(e):
    name=idEntry.get()
    if name == '':
        idEntry.insert(0,'Email')

#password
def on_enter(e):
    passwdEntry.delete(0, END)

def on_Leave(e):
    password = passwdEntry.get()
    if password == '':
        passwdEntry.insert(0, 'password')


#for hiding data on the entry fields by clicking on the check box
def show():
    passwdEntry.configure(show='*')
    check.configure(command=hide, text='')

def hide():
    passwdEntry.configure(show='')
    check.configure(command=show, text='')


#frame
# image_0=Image.open('C:\\Users\Igbon Ifijeh\Downloads\\pexels-dominika-roseclay-2682877.jpg')
# bck_pic=ImageTk.PhotoImage(image_0.resize((900,700)))
#
# lbl = Label(windows, image=bck_pic)
# lbl.place(x=1, y=1)

frame=Frame(windows, width=700, height=400, bg='black')
frame.place(x=0,y=0)


LogoImage=PhotoImage(file='email (1).png')
idlabel=Label(frame, text='Email', fg='#97FFFF', image=LogoImage, compound=LEFT, bg='black', font=('Calibre', 14, 'bold'))
idlabel.grid(row=1, column=0, pady=20, padx=3)



passwordImage=PhotoImage(file='padlock.png')
passwdlabel=Label(frame, image=passwordImage, compound=LEFT,fg='#97FFFF', bg='black', text='Password', font=('Calibre', 14, 'bold'))
passwdlabel.grid(row=3, column=0, pady=10, padx=3)


idEntry=Entry(frame, width=39, bd=3)
idEntry.grid(row=1,column=2,columnspan=2, padx=57)


passwdEntry=Entry(frame, width=39, bd=3)
passwdEntry.grid(row=3, column=2, columnspan=2)

#application of erasable text on the entry fields
idEntry.insert(0, '@email.com')
idEntry.bind('<FocusIn>', on_entry)
idEntry.bind('<FocusOut>', on_password)

passwdEntry.insert(0, "password")
passwdEntry.bind('<FocusIn>', on_enter)
passwdEntry.bind('<FocusOut>', on_Leave)



#btn
loginbtn=Button(frame, text='LOGIN', bg='#7f7fff', pady=10, width=23,fg='white', font=('open sans', 9, 'bold'), cursor='hand2', border=0, borderwidth=5, command=login)
loginbtn.grid(row=9,  columnspan=5, pady=30)


donthaveacctLabel=Label(frame, text='Don\'t have an account?', fg='#97FFFF', bg='black', pady=4, font=('Harrington', 9, 'bold'))
donthaveacctLabel.place(y=170)

createnewacct = Button(frame, width=15, text='Create One', border=0, bg='white', cursor='hand2', fg='black', font=('tahoma', 8, 'bold'), command=create_one)
createnewacct.place(x=10, y=199)

forgtpw=Button(frame, text='Forgot Password?', fg='#97FFFF',border=0, cursor='hand2', bg='black', font=('Harrington', 9, 'bold'), command=forgot_password)
forgtpw.place(x=310,y=120)


check = Checkbutton(frame, text='',
        command=show, bg='black')
check.place(x=440, y=100)


windows.mainloop()