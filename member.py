from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

class Registration:

    def __init__(self,root):
        self.root=root
        self.root.title("Member Registration System")
        self.root.configure(background='black')
        self.root.geometry("1350x750+0+0")


        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))


        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()


        FirstName=StringVar()
        SurName=StringVar()                
        Address=StringVar()
        Postcode=StringVar()        
        Telephone=StringVar()
        Ref=StringVar()                
        Date=StringVar()
                        
        Membership=StringVar()
        Membership.set("0")
        #=====================Function declaration=====================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("Member Registration system","Confirmation if you want to exit" )
            if iExit >0:
                root.destroy()
                return
        def Reset():
            
            FirstName.set("")
            SurName.set("")
            Address.set("")
            Postcode.set("")      
            Telephone.set("")
            Ref.set("")               
            Date.set("")
            
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)

        def iResetRecord():
            iResetRecord=tkinter.messagebox.askokcancel("Member Registration system","Confirm if you want to add a new record" )
            if iResetRecord >0:
                Reset()
            elif iResetRecord<=0:
                Reset()
                self.txtRecepit.delete("1.0",END)
                return
        def Ref_No():
            
            x=random.randint(10903,600873)
            randomRef=str(x)
            Ref.set(randomRef)
            
        def Recepit():
            Ref_No()
            self.txtRecepit.insert(END,"\t"+Ref.get()+"\t\t"+FirstName.get()+"\t\t"+ SurName.get()+"\t\t"+Address.get()+"\t\t"+
            DateofOrder.get() +"\t\t"+Telephone.get()+"\t\t"+Membership.get()+"\n" )
        def Membership_Fees():
            #global paid1
            if(var4.get()==1):
                self.txtMembership.configure(state=NORMAL)
                Item=float(50)
                Membership.set("rs."+ str(Item))
                #paid1=Membership.get()
            elif(var4.get()==0):
                self.txtMembership.configure(state=DISABLED)
            
                Membership.set("0")

        
        
        #=========================================frame===================================
        Mainframe=Frame(self.root)                
        Mainframe.grid()

        TitleFrame=Frame(Mainframe,bd=20,width=1350,padx=26,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lbTitle=Label(TitleFrame,font=('arial',59,'bold'),text="Member Registration system",padx=2)
        self.lbTitle.grid()

        #===================================Lowerframe===========================
        

        MemberFrameDetail=Frame(Mainframe,bd=20,width=1350,height=500,pady=5,relief=RIDGE)
        MemberFrameDetail.pack(side=BOTTOM)

        FrameDetails=LabelFrame(MemberFrameDetail,bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        
        MemberName_F=LabelFrame(FrameDetails,bd=10,width=350,height=400,padx=20,relief=RIDGE,
                            font=('arial',12,'bold'),text="Customer Name:")
        MemberName_F.grid(row=0,column=0)

        Recepit_Button=LabelFrame(MemberFrameDetail,bd=10,width=1000,height=400,relief=RIDGE)
        Recepit_Button.pack(side=RIGHT)
        #==========================================================================================
        self.lbReferenceNo=Label(MemberName_F,font=('arial',15,'bold'),text="Reference No:",bd=7,padx=2)
        self.lbReferenceNo.grid(row=0,column=0)
        self.txtReferenceNo=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,
                                  textvariable=Ref,state=DISABLED,insertwidth=2)
        self.txtReferenceNo.grid(row=0,column=1)


        self.lbFirstName=Label(MemberName_F,font=('arial',15,'bold'),text="First Name:",bd=7,padx=2)
        self.lbFirstName.grid(row=1,column=0)
        self.txtFirstName=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,
                                textvariable=FirstName,insertwidth=2)
        self.txtFirstName.grid(row=1,column=1)

        self.lbSurName=Label(MemberName_F,font=('arial',15,'bold'),text="Sur Name:",bd=7,padx=2)
        self.lbSurName.grid(row=2,column=0)
        self.txtSurName=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,insertwidth=2,
                              textvariable=SurName)
        self.txtSurName.grid(row=2,column=1)

        self.lbAddress=Label(MemberName_F,font=('arial',15,'bold'),text="Address:",bd=7,padx=2)
        self.lbAddress.grid(row=3,column=0)
        self.txtAddress=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,insertwidth=2,
                              textvariable=Address)
        self.txtAddress.grid(row=3,column=1)

        self.lbPostcode=Label(MemberName_F,font=('arial',15,'bold'),text="Post code:",bd=7,padx=2)
        self.lbPostcode.grid(row=4,column=0)
        self.txtPostcode=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,insertwidth=2,
                               textvariable=Postcode)
        self.txtPostcode.grid(row=4,column=1)

        self.lbTelephone=Label(MemberName_F,font=('arial',15,'bold'),text="Telephone:",bd=7,padx=2)
        self.lbTelephone.grid(row=5,column=0)
        self.txtTelephone=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,insertwidth=2
                                ,textvariable=Telephone)
        self.txtTelephone.grid(row=5,column=1)

        self.lbDate=Label(MemberName_F,font=('arial',15,'bold'),text="Date:",bd=7,padx=2)
        self.lbDate.grid(row=6,column=0)
        self.txtDate=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,insertwidth=2,
                           textvariable=DateofOrder)
        self.txtDate.grid(row=6,column=1)
        #======================================Member Information=================================
        self.lbProve_of_ID=Label(MemberName_F,font=('arial',15,'bold'),text="Prove of ID:",bd=7)
        self.lbProve_of_ID.grid(row=7,column=0,sticky=W)

        self.cboProve_of_ID=ttk.Combobox(MemberName_F,textvariable=var1,state='readonly',
                                        font=('arial',15,'bold'),width=19)
        self.cboProve_of_ID['value']=('','Pilot Licence','Driving Licence','Passport','Student ID')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7,column=1,sticky=W)


        self.lbType_of_Member=Label(MemberName_F,font=('arial',15,'bold'),text="Type_of_Member:",bd=7)
        self.lbType_of_Member.grid(row=8,column=0,sticky=W)

        self.cboType_of_Member=ttk.Combobox(MemberName_F,textvariable=var2,state='readonly',
                                        font=('arial',15,'bold'),width=19)
        self.cboType_of_Member['value']=('','Full Member','Annual Membership','Pay as You Go','Honorary Member')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1,sticky=W)

        self.lbMethod_of_Payment=Label(MemberName_F,font=('arial',15,'bold'),text="Method_of_Payment:",bd=7)
        self.lbMethod_of_Payment.grid(row=9,column=0,sticky=W)

        self.cboMethod_of_Payment=ttk.Combobox(MemberName_F,textvariable=var3,state='readonly',
                                        font=('arial',15,'bold'),width=19)
        self.cboMethod_of_Payment['value']=('','Visa Card','Master Card','Debit Card','Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9,column=1,sticky=W)
        #=============================CheckButton==========================
        self.chkMembership=Checkbutton(MemberName_F,font=('arial',16,'bold'),
        text="Membership Fees:",variable=var4,onvalue=1,bd=7,padx=2,command=Membership_Fees).grid(row=10,column=0,sticky=W)
        
        self.txtMembership=Entry(MemberName_F,font=('arial',15,'bold'),bd=7,insertwidth=2,
                           textvariable=Membership,state=DISABLED,justify=RIGHT)
        self.txtMembership.grid(row=10,column=1)
        #==============================================Receipt========================================
        
        self.lbLabel=Label(Recepit_Button,font=('arial',10,'bold'),text="Member Ref\t First Name\t Sur Name\t Address\t Date\t Reg\t Telephone\tMember Paid"
                           ,bd=7,pady=10)
        self.lbLabel.grid(row=0,column=0,columnspan=4)

        self.txtRecepit=Text(Recepit_Button,font=('arial',10,'bold'),width=112,height=22)
        self.txtRecepit.grid(row=1,column=0,columnspan=4)
        #========================Buttons=======================================================
        self.btnRecepit=Button(Recepit_Button,padx=18,bd=7,font=('arial',16,'bold'),width=13,text="Recepit",command=Recepit).grid(row=2,column=0)

        self.btnReset=Button(Recepit_Button,padx=18,bd=7,font=('arial',16,'bold'),width=13,text="Reset",command=iResetRecord).grid(row=2,column=1)

        self.btnExit=Button(Recepit_Button,padx=18,bd=7,font=('arial',16,'bold'),width=13,text="Exit",command=iExit).grid(row=2,column=2)

        









if __name__=='__main__':
    root=Tk()
    application=Registration(root)
    root.mainloop()
                       
                        
                    





















                        
    
