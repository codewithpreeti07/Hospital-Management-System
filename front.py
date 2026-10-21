from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root=Tk()
    app=Window1(root)


class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.LabelTitle = Label(self.frame,text="PHARMACY MANAGEMANT SYSTEM",fg="green",font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0, column=0,columnspan=2,pady=40)
        
        self.Loginframe1 = Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame,width=1000,height=200,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3, column=0,pady=2)
        #=====================================================================================
        self.lbUsername = Label(self.Loginframe1,text="Username",font=('arial',30,'bold'),bd=22)
        self.lbUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1,font=('arial',30,'bold'),bd=22,textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)


        self.lblPassword= Label(self.Loginframe1,text="Password",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword= Entry(self.Loginframe1,font=('arial',30,'bold'),bd=22,textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1,padx=85)
        
        #========================================================================================
        
                
        self.btnLogin = Button(self.Loginframe2,text="LOGIN",width=17,font=('arial',20,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)
        
        self.btnReset = Button(self.Loginframe2,text="RESET",width=17,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=0,column=1)

        self.btnExit = Button(self.Loginframe2,text="EXIT",width=17,font=('arial',20,'bold'),command=self.iExit)
        self.btnExit.grid(row=0,column=2)
        #===========================================================================================
        self.btnRegistration=Button(self.Loginframe3,text="PATITENT MANAGEMENT SYSTEM",
                                    state=DISABLED,command=self.Registration_window,font=('arial',20,'bold'))
        self.btnRegistration.grid(row=0,column=0)
        
        self.btnHospital = Button(self.Loginframe3,text="+HOSPITAL MANAGEMENT SYSTEM",
                                  state=DISABLED,command=self.Hospital_window,font=('arial',20,'bold'))
        self.btnHospital.grid(row=0,column=1)
        
        #================================================================================================
    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())

        if (user== str(1234))and (pas== str(2345)):
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=NORMAL)


        else:
            tkinter.messagebox.askyesno("Pharmacy Management System","You have enterd an invalid login details")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Pharmacy Management System","confirm if you want tp exit")
        if self.iExit >0:
            self.master.destroy()
            return
            

        
        #========================================================================
        
    def Registration_window(self):
        self.newWindow=Toplevel(self.master)
        self.app =Window2(self.newWindow)
        
    def Hospital_window(self):
        self.newWindow=Toplevel(self.master)
        self.app =Window3(self.newWindow)
        


class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Patient Registration system")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        #================================================================
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
        Mainframe=Frame(self.frame)                
        Mainframe.grid()

        TitleFrame=Frame(Mainframe,bd=20,width=1350,padx=26,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lbTitle=Label(TitleFrame,font=('arial',59,'bold'),text="MEMBER REGISTRATION SYSTEM",fg='red',padx=2)
        self.lbTitle.grid()

        #===================================Lowerframe===================Member========
        

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
        
        #============================================================================
    
class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("hospital management system")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        #=================================================================================
        cmbNameTablets=StringVar()
        Ref=StringVar()
        Dose=StringVar()
        NumberTablets=StringVar()
        Issuedate=StringVar()
        Expdate=StringVar()
        Dailydose=StringVar()
        PossibleSideEffect=StringVar()
        FurtherInformation=StringVar()
        StorageAdvice=StringVar()
        PatientId=StringVar()
        PatientName=StringVar()
        DateOfBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()

        #==============================Function Declaration=================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("+Hospital Management Mystem","Confirm if you want to exit" )
            if iExit >0:
                #root.destroy()
                return
        def iPrescription():
            self.txtPrescription.insert(END,'Name of Tablets:\t\t\t'+ cmbNameTablets.get()+"\n")
            self.txtPrescription.insert(END,'Reference No:\t\t\t'+ Ref.get()+"\n")
            self.txtPrescription.insert(END,'Dose:\t\t\t'+ Dose.get()+"\n")
            self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+NumberTablets.get()+"\n")
            self.txtPrescription.insert(END,'Issue Date:\t\t\t'+Issuedate.get()+"\n")
            self.txtPrescription.insert(END,'Expdate:\t\t\t'+Expdate.get()+"\n")
            self.txtPrescription.insert(END,'Daily dose:\t\t\t'+ Dailydose.get()+"\n")
            self.txtPrescription.insert(END,'Further Information:\t\t\t'+ FurtherInformation.get()+"\n")
            self.txtPrescription.insert(END,'Storage Advice:\t\t\t'+ StorageAdvice.get()+"\n")
            self.txtPrescription.insert(END,'Patient Id:\t\t\t'+ PatientId.get()+"\n")
            self.txtPrescription.insert(END,'Patient Name:\t\t\t'+ PatientName.get()+"\n")
            self.txtPrescription.insert(END,'Date Of Birth:\t\t\t'+ DateOfBirth.get()+"\n")
            self.txtPrescription.insert(END,'Patient Address:\t\t\t'+PatientAddress.get()+"\n")
            
            return
        def iDelete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Issuedate.set("")
            Expdate.set("")
            Dailydose.set("")
            PossibleSideEffect.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            PatientId.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            

            

            return
        def iReset():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Issuedate.set("")
            Expdate.set("")
            Dailydose.set("")
            PossibleSideEffect.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            PatientId.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            #self.txtFrameDetail.delete("1.0",END)

            return
        def iPrescriptionData():
            
            self.txtFrameDetail.insert(END,cmbNameTablets.get()+"\t"+Ref.get()+"\t"+ NumberTablets.get()+"\t"+Issuedate.get()+"\t"+
            Expdate.get() +"\t"+Dailydose.get()+"\t"+PossibleSideEffect.get()+"\t"+FurtherInformation.get()+"\t"+FurtherInformation.get()+
                                       "\t"+StorageAdvice.get()
                                  +"\t"+PatientId.get()+"\t"+ PatientName.get()+"\t"+ DateOfBirth.get()+"\t"+PatientAddress.get()+"\n" )
        
        #======================Frame=========================================================

        MainFrame=Frame(self.frame)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,bd=20,width=1350,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lbTitle=Label(TitleFrame,width=39,font=('arial',40,'bold'),text="+HOSPITAL MANAGEMENT SYSTEM",fg='red',padx=8)
        self.lbTitle.grid()
        
        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1450,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1450,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,
                            font=('arial',12,'bold'),text="Patient Information:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,
                                  font=('arial',12,'bold'),text="Prescription:")
        DataFrameRIGHT.pack(side=RIGHT)
        #========================================================DataFrameLEFT=============================================
        self.lbNameTablet=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Name of tablets",padx=4,pady=4)
        self.lbNameTablet.grid(row=0,column=0)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets,state='readonly',
                                        font=('arial',11,'bold'),)
        self.cboNameTablet['value']=('','Ibuprofem','Co-codmal','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1,sticky=W)

        self.lbFurtherInfo=Label(DataFrameLEFT,font=('arial',12,'bold'),text="FurtherInformation",padx=2,pady=2)
        self.lbFurtherInfo.grid(row=0,column=2,sticky=W)
        self.txtFurtherInfo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=FurtherInformation)
        self.txtFurtherInfo.grid(row=0,column=3)

        self.lbRef=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Reference",padx=2,pady=2)
        self.lbRef.grid(row=1,column=0,sticky=W)
        self.txtRef=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref)
        self.txtRef.grid(row=1,column=1)

        self.lbStorage=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Storage Advice",padx=2,pady=2)
        self.lbStorage.grid(row=1,column=2,sticky=W)
        self.txtStorage=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=StorageAdvice)
        self.txtStorage.grid(row=1,column=3)

        self.lbDose=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Dose",padx=2,pady=2)
        self.lbDose.grid(row=2,column=0,sticky=W)
        self.txtDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dose)
        self.txtDose.grid(row=2,column=1)

        self.lbExpdate=Label(DataFrameLEFT,font=('arial',12,'bold'),text=" Expire Date",padx=2,pady=2)
        self.lbExpdate.grid(row=4,column=0,sticky=W)
        self.txtExpdate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Expdate)
        self.txtExpdate.grid(row=4,column=1)

        self.lbIssuedate=Label(DataFrameLEFT,font=('arial',12,'bold'),text=" Issue Date",padx=2,pady=2)
        self.lbIssuedate.grid(row=3,column=0,sticky=W)
        self.txtIssuedate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Issuedate)
        self.txtIssuedate.grid(row=3,column=1)

        self.lbDailydose=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Dailydose",padx=2,pady=2)
        self.lbDailydose.grid(row=5,column=0,sticky=W)
        self.txtDailydose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dailydose)
        self.txtDailydose.grid(row=5,column=1)

        self.lbPossibleSideEffect=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Possible Side Effect",padx=2,pady=2)
        self.lbPossibleSideEffect.grid(row=2,column=2,sticky=W)
        self.txtPossibleSideEffect=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PossibleSideEffect)
        self.txtPossibleSideEffect.grid(row=2,column=3)

        self.lbPatientId=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Id",padx=2,pady=2)
        self.lbPatientId.grid(row=4,column=2,sticky=W)
        self.txtPatientId=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientId)
        self.txtPatientId.grid(row=4,column=3)

        self.lbPatientName=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Name",padx=2,pady=2)
        self.lbPatientName.grid(row=3,column=2,sticky=W)
        self.txtPatientName=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientName)
        self.txtPatientName.grid(row=3,column=3)

        self.lbDateOfBirth=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date Of Birth",padx=2,pady=2)
        self.lbDateOfBirth.grid(row=5,column=2,sticky=W)
        self.txtDateOfBirth=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DateOfBirth)
        self.txtDateOfBirth.grid(row=5,column=3)

        self.lbPatientAddress=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Address",padx=2,pady=2)
        self.lbPatientAddress.grid(row=6,column=2,sticky=W)
        self.txtPatientAddress=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientAddress)
        self.txtPatientAddress.grid(row=6,column=3)
        
        self.lbNumberTablets=Label(DataFrameLEFT,font=('arial',12,'bold'),text="No of Tablets",padx=2,pady=2)
        self.lbNumberTablets.grid(row=6,column=0,sticky=W)
        self.txtNumberTablets=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=NumberTablets)
        self.txtNumberTablets.grid(row=6,column=1)
        #==========================DATAFRAMERIGHT==================================================

        self.txtPrescription=Text(DataFrameRIGHT,font=('arial',12,'bold'),width=43,height=14,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #==================================Frame Details====================================
        self.lbLabel=Label(FrameDetail,font=('arial',10,'bold'),pady=8,
        text="\t Name of Tablet\t Reference No\t No of tablets\t Issue date\t Expire date\t Daily Dose\tStorage Adv\tPatient Id\t Patient Name\t DOB\t Address\t Dose\tSide effect",)
        self.lbLabel.grid(row=0,column=0)
        
        self.txtFrameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)

        #========================================ButtonFrame==================================
        self.btnPrescription=Button(ButtonFrame,text='Prescription',font=('arial',12,'bold'),width=24,bd=4,
                                    command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)

        self.btnPrescriptionData=Button(ButtonFrame,text="Prescription Data",font=('arial',12,'bold'),width=24,bd=4,
                               command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),width=24,bd=4,
                              command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        
        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),width=24,bd=4,
                             command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btniExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width=24,bd=4,command=iExit)
        self.btniExit.grid(row=0,column=4)
              
        #=============================================================================
        
        
        


if __name__=='__main__':
    main()
