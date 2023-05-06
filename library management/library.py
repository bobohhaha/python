from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class librarymanagemnt:
    def __init__(self,root):
        self.root=root
        self.root.title("library managemnt system")
        self.root.geometry("1550x800+0+0")

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMNT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6) 
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(frame,text="Library Membership information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("arial",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="member Type:",font=("arial",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",15,"bold"),width=25,state="readonly")
        comMember["value"]=("Admin Staf","student","lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN NO:",font=("arial",11,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        TxtPRN_No=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",12,"bold"),width=26)
        TxtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID NO:",font=("arial",11,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",12,"bold"),width=26)
        txtTitle.grid(row=2,column=1)

        lblfirstname=Label(DataFrameLeft,bg="powder blue",text="FirstName:",font=("arial",11,"bold"),padx=2,pady=6)
        lblfirstname.grid(row=3,column=0,sticky=W)
        txtfirstname=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",12,"bold"),width=26)
        txtfirstname.grid(row=3,column=1)

        lbllastname=Label(DataFrameLeft,bg="powder blue",text="LastName:",font=("arial",11,"bold"),padx=2,pady=6)
        lbllastname.grid(row=4,column=0,sticky=W)
        txtlastname=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",12,"bold"),width=26)
        txtlastname.grid(row=4,column=1)

        lblAdress1=Label(DataFrameLeft,bg="powder blue",text="Adresse1:",font=("arial",11,"bold"),padx=2,pady=6)
        lblAdress1.grid(row=5,column=0,sticky=W)
        txtAdress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",12,"bold"),width=26)
        txtAdress1.grid(row=5,column=1)

        lblAdress2=Label(DataFrameLeft,bg="powder blue",text="Adresse2:",font=("arial",11,"bold"),padx=2,pady=6)
        lblAdress2.grid(row=6,column=0,sticky=W)
        txtAdress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",12,"bold"),width=26)
        txtAdress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post code:",font=("arial",11,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",12,"bold"),width=26)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile:",font=("arial",11,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",12,"bold"),width=26)
        txtMobile.grid(row=8,column=1)

        lblBookid=Label(DataFrameLeft,bg="powder blue",text="Book Id:",font=("arial",10,"bold"),padx=2)
        lblBookid.grid(row=0,column=2,sticky=W)
        txtBookid=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",10,"bold"),width=26)
        txtBookid.grid(row=0,column=3)

        lblBooktitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",10,"bold"),padx=2,pady=6)
        lblBooktitle.grid(row=1,column=2,sticky=W)
        txtBooktitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",10,"bold"),width=26)
        txtBooktitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="powder blue",text="Auther Name:",font=("arial",10,"bold"),padx=2,pady=6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,textvariable=self.auther_var,font=("arial",10,"bold"),width=26)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("arial",10,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",10,"bold"),width=26)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("arial",10,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",10,"bold"),width=26)
        txtDateDue.grid(row=4,column=3)
        
        lblDaysonbook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("arial",10,"bold"),padx=2,pady=6)
        lblDaysonbook.grid(row=5,column=2,sticky=W)
        txtDaysonbook=Entry(DataFrameLeft,textvariable=self.daysonbook,font=("arial",10,"bold"),width=26)
        txtDaysonbook.grid(row=5,column=3)

        lbllatereturn=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("arial",10,"bold"),padx=2,pady=6)
        lbllatereturn.grid(row=6,column=2,sticky=W)
        txtlatereturn=Entry(DataFrameLeft,textvariable=self.lateratefine_var,font=("arial",10,"bold"),width=26)
        txtlatereturn.grid(row=6,column=3)

        lblDateoverdate=Label(DataFrameLeft,bg="powder blue",text="Date over Due:",font=("arial",10,"bold"),padx=2,pady=6)
        lblDateoverdate.grid(row=7,column=2,sticky=W)
        txtDateoverdate=Entry(DataFrameLeft,textvariable=self.dateoverdue,font=("arial",10,"bold"),width=26)
        txtDateoverdate.grid(row=7,column=3)

        lblActualePrice=Label(DataFrameLeft,bg="powder blue",text="actual price:",font=("arial",10,"bold"),padx=2,pady=6)
        lblActualePrice.grid(row=8,column=2,sticky=W)
        txtActualprice=Entry(DataFrameLeft,textvariable=self.finallprice,font=("arial",10,"bold"),width=26)
        txtActualprice.grid(row=8,column=3)

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("arial",15,"bold"),padx=20)
        DataFrameRight.place(x=870,y=5,width=580,height=350)

        self.txtbox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=15,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight,width=25)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        Listbooks=['learn python','learn c++','learn java','learn java secript','learn c','learn c#','learn arabic','learn frenche','learn english','emsi ntg','my life from 0 to top','My python','machine tecno','advance python',
                 'machine learning','python box','i love python','How me learn','make it stick','art of learning','deep work','fluent forever','brain rules','how to learn','lapprentissage profond','atteinder lexcellence','why we sleep'
                        ]
        def selectBook(event=""):
            value=str(ListBox.get(ListBox.curselection()))
            x=value
            if(x=="learn python"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("python manual")
                self.auther_var.set("paul Berry")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue.set("No")
                self.finallprice.set("Rs.788")

        
        ListBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        ListBox.bind("<<Listboxselect>>",selectBook)
        ListBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=ListBox.yview)

        for item in Listbooks:
            ListBox.insert(END,item)

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data", font=("arial", 12, "bold"),width=23,bg="blue",fg="white",pady=7,padx=3)
        btnAddData.grid(row=0,column=0)        

        btnAddData=Button(Framebutton,text="Show Data",command=self.showData, font= ("arial",12, "bold"),width=23, bg="blue",fg="white",pady=7,padx=3)
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",command=self.update, font= ("arial",12, "bold"),width=23, bg="blue",fg="white",pady=7,padx=3)
        btnAddData.grid(row=0,column=2)

        btnAddData=Button (Framebutton,text="Delete",command=self.delete, font= ("arial", 12, "bold"),width=23,bg="blue",fg="white",pady=7,padx=3)
        btnAddData.grid(row=0,column=3)

        btnAddData=Button (Framebutton,text="Reset",command=self.reset ,font=("arial",12,"bold"),width=23,bg="blue",fg="white",pady=7,padx=3)
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit", command=self.iExit,font=("arial", 12, "bold"),width=23,bg="blue",fg="white",pady=7,padx=3)
        btnAddData.grid(row=0,column=5)
        


        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=170)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("memebertype", "prnno", "title", "firtname", "lastname", "address1",
        "address2", "postid", "mobile", "bookid", "booktitle", "auther", "dateborrowed","datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memebertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firtname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Adresse1")
        self.library_table.heading("address2",text="Adresse2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther" )
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table[ "show" ]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("memebertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firtname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finallprice.get()  
                                                                                                                ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("success","Member Has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,firtname=%s,lastname=%s,address1=%s,address2=%s,postid=%s,Mobile=%s,bookid=%s,booktitle=%s,Auther=%s,dateborrowed=%s,datedue=%s,daysofbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finallprice.get()
                                                                                                                

                            ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("succes","Member Has been updated")
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finallprice.set(row[17])

    def showData(self):
        self.txtbox.insert(END,"memebertype\t\t"+self.member_var.get()+"\n")
        self.txtbox.insert(END,"prnno \t\t"+self.prn_var.get()+"\n")
        self.txtbox.insert(END,"Ititle\t\t"+self.id_var.get()+"\n")
        self.txtbox.insert(END,"firtname:\t\t"+self.firstname_var.get()+"\n")
        self.txtbox.insert(END,"lastname\t\t"+self.lastname_var.get()+"\n")
        self.txtbox.insert(END,"address1\t\t"+self.address1_var.get()+"\n")
        self.txtbox.insert(END,"address2\t\t"+self.address2_var.get()+"\n")
        self.txtbox.insert(END,"postid\t\t"+self.postcode_var.get()+"\n")
        self.txtbox.insert(END,"mobile\t\t"+self.mobile_var.get()+"\n")
        self.txtbox.insert(END,"bookid\t\t"+self.bookid_var.get()+"\n")
        self.txtbox.insert(END,"booktitle\t\t"+self.booktitle_var.get()+"\n")
        self.txtbox.insert(END,"auther\t\t"+self.auther_var.get()+"\n")
        self.txtbox.insert(END,"dateborrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtbox.insert(END,"datedue\t\t"+self.datedue_var.get()+"\n")
        self.txtbox.insert(END,"days\t\t"+self.daysonbook.get()+"\n")
        self.txtbox.insert(END,"latereturnfine\t\t"+self.lateratefine_var.get()+"\n")
        self.txtbox.insert(END,"dateoverdue\t\t"+self.dateoverdue.get()+"\n")
        self.txtbox.insert(END,"finalprice\t\t"+self.finallprice.get()+"\n")

    def reset(self):
         self.member_var.set(""),
         self.prn_var.set(""),
         self.id_var.set(""),
         self.firstname_var.set(""),
         self.lastname_var.set(""),
         self.address1_var.set(""),
         self.address2_var.set(""),
         self.postcode_var.set(""),
         self.mobile_var.set(""),
         self.bookid_var.set(""),
         self.booktitle_var.set(""),
         self.auther_var.set(""),
         self.dateborrowed_var.set(""),
         self.datedue_var.set(""),
         self.daysonbook.set(""),
         self.lateratefine_var.set(""),
         self.dateoverdue.set(""),
         self.finallprice.set("")
         self.txtbox.delete("1.0",END)
    
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="" :
            messagebox.showerror("error","First select the member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get())
            my_cursor.execute(query,value)

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Succes","Member has been Deleted")

    
if __name__ == "__main__":
    root=Tk()
    obj=librarymanagemnt(root)
    root.mainloop()
