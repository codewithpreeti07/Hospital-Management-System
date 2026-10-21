from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry('1350x750+0+0')
       

        lbtitle=Label(self.root,bd=20,fg="red",bg="white",font=('arial',40,'bold'),text="+ HOSPITAL MANAGEMENT SYSTEM",relief=RIDGE)
        lbtitle.pack(side=TOP,fill=X)

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1550,height=400)

        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=900,height=350,padx=20,relief=RIDGE,
                            font=('arial',12,'bold'),text="Patient Information:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,
                                  font=('arial',12,'bold'),text="Prescription:")
        DataFrameRIGHT.pack(side=RIGHT)
        



        
        






        

root=Tk()
ob=Hospital(root)
root.mainloop()
    
