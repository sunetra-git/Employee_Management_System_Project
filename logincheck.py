from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import Employee_Dbms as em
root1 = Tk()
root1.title("Employee Management System")
 
width = 640
height = 480
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root1.geometry("%dx%d+%d+%d" % (width, height, x, y))
root1.resizable(0, 0)


USERNAME = StringVar()
PASSWORD = StringVar()

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")


def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root1)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
   
def ToggleToLogin(event=None):
    LoginForm()

def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
            em.Employee()
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
LoginForm()

menubar = Menu(root1)
filemenu = Menu(menubar, tearoff=0)
root1.config(menu=menubar)


if __name__ == '__main__':
    root1.mainloop()
   
