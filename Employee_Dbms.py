from tkinter import *
import tkinter.messagebox
import sqlite3
class Employee:
    def __init__(self,root):
        p=Database()
        p.conn()
        self.root=root
        self.root.title("EMPLOYEE MANEGEMENT SYSTEM")
        self.root.geometry("1300x7500+0+0")
        self.root.config(bg="cadet blue")
        EmpId=StringVar()
        firstname=StringVar()
        lastname=StringVar()
        dob=StringVar()
        def close():
            print("employee:close method called")
            close=tkinter.messagebox.askyesno("EMPLOYEE MANAGEMENT SYSTEM","confirm if you want to exit")
            if(close>0):
                root.destroy()
                print("employee:close method finished\n")
                return
        def clearData():
            print("employee:clear method called")
            self.txtEmpId.delete(0,END)
            self.txtEmpfna.delete(0,END)
            self.txtEmplna.delete(0,END)
            self.txtEmpdob.delete(0,END)
            self.txtEmpage.delete(0,END)
            self.txtEmpgen.delete(0,END)
            self.txtEmpadd.delete(0,END)
            self.txtEmpms.delete(0,END)
            self.txtEmpemail.delete(0,END)
            self.txtEmpmob.delete(0,END)
            print("employee:clear method finished\n")
        
        def insert():
            print("employee:insert method called")
            if(len(EmpId.get())!=0):
                p.insert(EmpId.get(),firstname.get(),lastname.get(),dob.get())
                Emplist.delete(0,END)
                Emplist.insert(END,EmpId.get(),firstname.get(),lastname.get(),dob.get())
            else:
                tkinter.messagebox.showwarning("EMPLOYEE MANAGEMENT SYSTEM","Atleast enter Employee ID")
            print("employee:insert method finished\n")
       
        MainFrame=Frame(self.root,bg="cadet blue")
        MainFrame.grid()
        TitFrame=Frame(MainFrame,bd=2,padx=54,pady=8,bg="ghost white",relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit=Label(TitFrame,font=('algerian',45,'bold'),text="EMPLOYEE MANAGEMENT SYSTEM",bg="ghost white",fg="brown")
        self.lblTit.grid()
        ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=5,bg="pink",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame=Frame(MainFrame,bd=2,width=1300,height=400,padx=20,pady=20,bg="cadet blue",relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=100,height=600,padx=20,pady=3,bg="ghost white",relief=RIDGE,font=('arial',22,'bold'),fg="purple",text="EMPLOYEE INFORMATION\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=100,height=1000,padx=20,pady=30,bg="ghost white",relief=RIDGE,font=('arial',22,'bold'),fg="purple",text="EMPLOYEE DETAILS\n")
        DataFrameRIGHT.pack(side=RIGHT)
        self.lblEmpId=Label(DataFrameLEFT,font=('arial',20,'bold'),text="Employee ID:",padx=2,pady=2,bg="ghost white")
        self.lblEmpId.grid(row=0,column=0,sticky=W)
        self.txtEmpId=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=EmpId,width=39)
        self.txtEmpId.grid(row=0,column=1)
        self.lblEmpfna=Label(DataFrameLEFT,font=('arial',20,'bold'),text="First Name:",padx=2,pady=2,bg="ghost white")
        self.lblEmpfna.grid(row=1,column=0,sticky=W)
        self.txtEmpfna=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=firstname,width=39)
        self.txtEmpfna.grid(row=1,column=1)
        self.lblEmplna=Label(DataFrameLEFT,font=('arial',20,'bold'),text="Last Name:",padx=2,pady=2,bg="ghost white")
        self.lblEmplna.grid(row=2,column=0,sticky=W)
        self.txtEmplna=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=lastname,width=39)
        self.txtEmplna.grid(row=2,column=1)
        self.lblEmpdob=Label(DataFrameLEFT,font=('arial',20,'bold'),text="Date Of Birth(DD/MM/YYYY):",padx=2,pady=2,bg="ghost white")
        self.lblEmpdob.grid(row=3,column=0,sticky=W)
        self.txtEmpdob=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=dob,width=39)
        self.txtEmpdob.grid(row=3,column=1)
        
        self.btnAddData=Button(ButtonFrame,text="SAVE",font=('comic san',22,'bold'),height=1,width=8,bd=4,command=insert)
        self.btnAddData.grid(row=0,column=0)
        
        self.btnClearData=Button(ButtonFrame,text="RESET",font=('comic san',22,'bold'),height=1,width=8,bd=4,command=clearData)
        self.btnClearData.grid(row=0,column=2)
        
        self.btnExitData=Button(ButtonFrame,text="EXIT",font=('comic san',22,'bold'),height=1,width=8,bd=4,command=close)
        self.btnExitData.grid(row=0,column=6)
class Database:
    def conn(self):
        print("Database: connection method called")
        con=sqlite3.connect("Employee1.db")
        cur=con.cursor()
        query="create table if not exists employee(EmpID integer primary key,\
                Firstname text,Lastname text,DOB text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database:Connection method finished\n")
    def insert(self,EmpID,Firstname,Lastname,DOB):
        print("Database: insert method called")
        con=sqlite3.connect("Employee1.db")
        cur=con.cursor()
        query="insert into employee values(?,?,?,?)"
        cur.execute(query,(EmpID,Firstname,Lastname,DOB))
        con.commit()
        con.close()
        print("Database:insert method finished\n")      
if __name__=='__main__':
    root=Tk()
    application=Employee(root)
    root.mainloop()

