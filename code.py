from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import width
import pymysql


class ConnectorDB:

    def __init__(self,root):
        self.root=root
        titlespace=" "
        self.root.title(102*titlespace+"MYSQL Connector")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd=10,width=770, height=700,relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7,width=770, height=100,relief = RIDGE)
        TitleFrame.grid(row = 0, column =0 )
        TopFrame3 = Frame(MainFrame , bd=5,width=770, height=500,relief = RIDGE)
        TopFrame3.grid(row= 1 , column = 0)


        LeftFrame = Frame(TopFrame3, bd=5,width=770, height=400, padx=2, bg= "Cadet blue",relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame , bd=5,width=600, height=180,padx=2, pady=4,relief = RIDGE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)
        

        RightFrame1 = Frame(TopFrame3, bd=5,width=100, height=400, padx=2, bg= "Cadet blue",relief = RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1 , bd=5,width=90, height=300,padx=2, pady=2,relief = RIDGE)
        RightFrame1a.pack(side=TOP)
        # =====================================variables=============================================================
        
        BookID=StringVar()
        BookGenre=StringVar()
        BookLang=StringVar()
        BookName=StringVar()
        BookAuth=StringVar()
        Publishyear=StringVar()
        Bookcopy=StringVar()
        BookPrice=StringVar()

         # ============================================Functions for the manipulation======================================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("MYSQL Connection","Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        def Reset():
            self.entBookID.delete(0,END)
            self.entBookGenre.delete(0,END)
            self.entBookLang.delete(0,END)
            self.entBookName.delete(0,END)
            self.entBookAuth.delete(0,END)
            self.entPublishyear.delete(0,END)
            self.entBookcopy.delete(0,END)
            self.entBookPrice.delete(0,END)
        def addData():
            if BookID.get()== "" or BookGenre.get()=="" or BookLang.get()=="" or BookName.get()=="" or BookAuth.get()=="" or Publishyear.get()=="" or Bookcopy.get()=="" or BookPrice.get()=="" :
                tkinter.messagebox.showerror("MYSql Connection","Enter correct Details")
            else:
                sqlCon= pymysql.connect(host="localhost",user="root",password="Aparna@19",database="book_management")
                cur=sqlCon.cursor()
                cur.execute("Insert into Book_Management values(%s,%s,%s,%s,%s,%s,%s,%s)",(BookID.get(),BookGenre.get(),BookLang.get(),BookName.get(),BookAuth.get(),Publishyear.get(),Bookcopy.get(),BookPrice.get()))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")

        def DisplayData():
            sqlCon= pymysql.connect(host="localhost",user="root",password="Aparna@19",database="book_management")
            cur=sqlCon.cursor()
            cur.execute("select * from book_management")
            result=cur.fetchall()
            if len(result) !=0:
                self.books.delete(*self.books.get_children())
                for row in result:
                    self.books.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Displayed Successfully")
            
            
        def TraineeInfo(ev):
            viewInfo = self.books.focus()
            learnerData = self.books.item(viewInfo)
            row = learnerData['values']
            BookID.set(row[0]),BookGenre.set(row[1]),BookLang.set(row[2]),BookName.set(row[3]),BookAuth.set(row[4]),Publishyear.set(row[5]),Bookcopy.set(row[6]),BookPrice.set(row[7])

        def update():
            sqlCon= pymysql.connect(host="localhost",user="root",password="Aparna@19",database="book_management")
            cur=sqlCon.cursor()
            cur.execute("update book_management set Book_Genre=%s,Book_Lang=%s,Book_Name=%s,Book_Auth=%s,Publish_year=%s,Book_copy=%s,Book_Price=%s where Book_Id= %s",(BookGenre.get(),BookLang.get(),BookName.get(),BookAuth.get(),Publishyear.get(),Bookcopy.get(),BookPrice.get(),BookID.get()))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")
        
        def delete():
            sqlCon= pymysql.connect(host="localhost",user="root",password="Aparna@19",database="book_management")
            cur=sqlCon.cursor()
            cur.execute("delete from book_management where Book_Id= %s",BookID.get())
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Deleted Successfully")
            Reset()

        def searchdb():
            try:
                sqlCon= pymysql.connect(host="localhost",user="root",password="Aparna@19",database="book_management")
                cur=sqlCon.cursor()
                cur.execute("select * from book_management where Book_Id= %s",BookID.get())
                row=cur.fetchall()

                BookID.set(row[0]),BookGenre.set(row[1]),BookLang.set(row[2]),BookName.set(row[3]),BookAuth.set(row[4]),Publishyear.set(row[5]),Bookcopy.set(row[6]),BookPrice.set(row[7])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","NO Such Record Found")
                Reset()
            sqlCon.close()
            

        # ==================================================================================================
        self.lbltitle=Label(TitleFrame,font=('arial',40, 'bold'),text="Book Management",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)
         # ==================================================================================================
        self.lblBookID=Label(LeftFrame1,font=('arial',12, 'bold'),text="Book ID",bd=7)
        self.lblBookID.grid(row=0,column=0,sticky=W,padx=5)
        self.entBookID=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BookID)
        self.entBookID.grid(row=0,column=1,sticky=W,padx=5)
        
        self.lblBookGenre=Label(LeftFrame1,font=('arial',12, 'bold'),text="Book Genre",bd=7)
        self.lblBookGenre.grid(row=1,column=0,sticky=W,padx=5)
        self.entBookGenre=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BookGenre)
        self.entBookGenre.grid(row=1,column=1,sticky=W,padx=5)

        self.lblBookLang=Label(LeftFrame1,font=('arial',12, 'bold'),text="Book Language",bd=7)
        self.lblBookLang.grid(row=2,column=0,sticky=W,padx=5)
        self.entBookLang=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BookLang)
        self.entBookLang.grid(row=2,column=1,sticky=W,padx=5)

        self.lblBookName=Label(LeftFrame1,font=('arial',12, 'bold'),text="Book Name",bd=7)
        self.lblBookName.grid(row=3,column=0,sticky=W,padx=5)
        self.entBookName=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BookName)
        self.entBookName.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblBookAuth=Label(LeftFrame1,font=('arial',12, 'bold'),text="Book Author",bd=7)
        self.lblBookAuth.grid(row=4,column=0,sticky=W,padx=5)
        self.entBookAuth=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BookAuth)
        self.entBookAuth.grid(row=4,column=1,sticky=W,padx=5)

        self.lblPublishyear=Label(LeftFrame1,font=('arial',12, 'bold'),text="Publish Year",bd=7)
        self.lblPublishyear.grid(row=5,column=0,sticky=W,padx=5)
        self.entPublishyear=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=Publishyear)
        self.entPublishyear.grid(row=5,column=1,sticky=W,padx=5)

        self.lblBookcopy=Label(LeftFrame1,font=('arial',12, 'bold'),text="Book copy",bd=7)
        self.lblBookcopy.grid(row=6,column=0,sticky=W,padx=5)
        self.entBookcopy=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=Bookcopy)
        self.entBookcopy.grid(row=6,column=1,sticky=W,padx=5)

        self.lblBookPrice=Label(LeftFrame1,font=('arial',12, 'bold'),text="Book Price",bd=7)
        self.lblBookPrice.grid(row=7,column=0,sticky=W,padx=5)
        self.entBookPrice=Entry(LeftFrame1,font=('arial',12, 'bold'),bd=5,width=44,justify='left',textvariable=BookPrice)
        self.entBookPrice.grid(row=7,column=1,sticky=W,padx=5)
        # ==========================================Table TreeView===================================================
        scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)

        self.books=ttk.Treeview(LeftFrame,height=12,columns=("Book_Id","Book_Genre","Book_Lang","Book_Name","Book_Auth","Publish_year","Book_copy","Book_Price"), yscrollcommand= scroll_y.set)
        
        scroll_y.pack(side= RIGHT,fill=Y)

        self.books.heading("Book_Id",text="BookID")
        self.books.heading("Book_Genre",text="BookGenre")
        self.books.heading("Book_Lang",text="BookLang")
        self.books.heading("Book_Name",text="BookName")
        self.books.heading("Book_Auth",text="BookAuthor")
        self.books.heading("Publish_year",text="Publishyear")
        self.books.heading("Book_copy",text="BookCopy")
        self.books.heading("Book_Price",text="BookPrice")
        
        self.books['show']='headings'

        self.books.column("Book_Id", width=20)
        self.books.column("Book_Genre", width=40)
        self.books.column("Book_Lang", width=40)
        self.books.column("Book_Name", width=60)
        self.books.column("Book_Auth", width=50)
        self.books.column("Publish_year", width=30)
        self.books.column("Book_copy", width=20)
        self.books.column("Book_Price", width=30)
        
        self.books.pack(fill=BOTH,expand=1)
        self.books.bind("<ButtonRelease-1>",TraineeInfo)
        # DisplayData()


        # =============================================================================================
        self.btnAddNew=Button(RightFrame1a,font=('arial',16, 'bold'),text="Add New",bd=4,pady=1,padx=24,width=8,height=2,command=addData).grid(row=0,column=0,padx=1)

        self.btnDisplay=Button(RightFrame1a,font=('arial',16, 'bold'),text="Display",bd=4,pady=1,padx=24,width=8,height=2,command=DisplayData).grid(row=1,column=0,padx=1)

        self.btnUpdate=Button(RightFrame1a,font=('arial',16, 'bold'),text="Update",bd=4,pady=1,padx=24,width=8,height=2,command=update).grid(row=2,column=0,padx=1)

        self.btnDelete=Button(RightFrame1a,font=('arial',16, 'bold'),text="Delete",bd=4,pady=1,padx=24,width=8,height=2,command=delete).grid(row=3,column=0,padx=1)

        self.btnSearch=Button(RightFrame1a,font=('arial',16, 'bold'),text="Search",bd=4,pady=1,padx=24,width=8,height=2,command=searchdb).grid(row=4,column=0,padx=1)

        self.btnReset=Button(RightFrame1a,font=('arial',16, 'bold'),text="Reset",bd=4,pady=1,padx=24,width=8,height=2,command=Reset).grid(row=5,column=0,padx=1)

        self.btnExit=Button(RightFrame1a,font=('arial',16, 'bold'),text="Exit",bd=4,pady=1,padx=24,width=8,height=2,command=iExit).grid(row=6,column=0,padx=1)
        # =============================================================================================
        
if __name__=='__main__':
    root=Tk()
    application=ConnectorDB(root)
    root.mainloop()