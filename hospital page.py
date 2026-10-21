from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


class Hospital:
    def __init__(self,master):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry('1700x1000+0+0')
        self.root.configure(background="powder blue")


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
            iExit=tkinter.messagebox.askyesno("Hospital Management Mystem","Confirm if you want to exit" )
            if iExit >0:
                root.destroy()
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

        MainFrame=Frame(self.root)
        MainFrame.grid()

        TitleFrame=Frame( MainFrame,bd=20,width=1350,padx=0,pady=0,relief=RIDGE)
        TitleFrame.pack(side=TOP,fill=X)
        
        self.lbTitle=Label(TitleFrame,bd=20,fg="red",bg="white",font=('arial',40,'bold'),text="+ HOSPITAL MANAGEMENT SYSTEM")
        self.lbTitle.grid()
        
        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
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
        















        
        






        
if __name__=='__main__':
    root=Tk()
    application=Hospital(root)
    root.mainloop()
    

        
        



























        
        
