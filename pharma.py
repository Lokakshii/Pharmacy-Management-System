from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")


        #----------addMed variable------
        self.ref_var= StringVar()
        self.addmed_var=StringVar()


        #---- main table variables-----
        self.refv=StringVar()
        self.compNamev=StringVar()
        self.typeMedv=StringVar()
        self.medNamev=StringVar()
        self.lotv=StringVar()
        self.issueDatev=StringVar()
        self.expDatev=StringVar()
        self.usesv=StringVar()
        self.sideeffectv=StringVar()
        self.warningv=StringVar()
        self.dosagev=StringVar()
        self.pricev=StringVar()
        self.productqtv=StringVar()
 

        #ye hai title ke liye
        lbltitle= Label(self.root, text= " PHARMACY MANAGEMENT SYSTEM", bd=15, relief= RIDGE
                        , bg='white', fg='darkblue', font=("Times New Roman", 40,'bold'), padx=2,pady=4)

        lbltitle.pack(side= TOP, fill=X)

        #ye hai image ke liye
        img1= Image.open("D:\\pharma prjt_sql&py\\logo.jpg") #use \\ not \
        img1= img1.resize((80,68), Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
        b1= Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=15, y=15)

        #----------DATAFRAME---------------
        #ye hai middle frames ke liye
        Dataframe= Frame(self.root, bd=15, relief=RIDGE, padx=20)
        Dataframe.place(x=0, y=90, width=1280, height=400)

        DataframeLeft= LabelFrame(Dataframe,  bd=10, relief=RIDGE, pady=12, padx=12, text="Medicine Information", fg= "purple", font=("Times New Roman", 15,'bold'))
        DataframeLeft.place(x=0, y=5, width=800, height=350)

        DataframeRight= LabelFrame(Dataframe, bd=10, relief=RIDGE,padx=12, pady=12, text="Medicine Add Dept", fg= "purple", font=("Times New Roman", 15,'bold'))
        DataframeRight.place(x=820, y=5, width=390, height=350)

        
        # ye frame  hai button  ke liye
        Buttonframe= Frame(self.root, bd=15, relief=RIDGE, padx=0)
        Buttonframe.place(x=0, y=460, width=1280, height=65)
        
        # for MAIN buttons it self
        btnAddData= Button(Buttonframe,command=self.add_data ,width=10,text="Medicine Add", font=("Times New Roman", 12,'bold'), bg= "Teal", fg="white")
        btnAddData.grid(row=0, column=0)
        
        btnUpdateMed= Button(Buttonframe,width=10, text="Update", font=("Times New Roman", 13,'bold'), bg= "teal", fg="white",  command=self.Update)
        btnUpdateMed.grid(row=0, column=1)
        
        btnDeleteMed= Button(Buttonframe,width=10, text="Delete", font=("Times New Roman", 13,'bold'), bg= "coral", fg="white", command=self.Delete)
        btnDeleteMed.grid(row=0, column=2)
        
        btnResetMed= Button(Buttonframe,width=10, text="Reset", font=("Times New Roman", 13,'bold'), bg= "Teal", fg="white", command= self.Clear)
        btnResetMed.grid(row=0, column=3)

        btnExitMed= Button(Buttonframe,width=10, text="Exit", font=("Times New Roman", 13,'bold'), bg= "coral", fg="white")
        btnExitMed.grid(row=0, column=4)
        

        #search by button
        lblsearch= Label(Buttonframe, text="Search by:", font=("Times New Roman", 15,'bold'),padx=2, bg= "lightblue", fg="white")
        lblsearch.grid(row=0, column=5, sticky=W)
        
        self.search_var=StringVar()
        search_combo= ttk.Combobox(Buttonframe, textvariable=self.search_var ,width=12,font=("Times New Roman", 15,'bold'), state="readonly")
        search_combo["values"]= ("Choose:","Ref", "Medname", "Lot" )
        search_combo.grid(row=0, column=6)
        search_combo.current(0)

        self.searchtxt_var= StringVar()        
        textSearch= Entry(Buttonframe,textvariable=self.searchtxt_var, bd=3, relief=RIDGE,font=("Times New Roman", 13,'bold'))
        textSearch.grid(row=0, column=7)

        SearchBtn = Button(Buttonframe, width=14, command=self.search_data, text="Search here", font=("Times New Roman", 12, 'italic'), bg="teal", fg="white")
        SearchBtn.grid(row=0, column=8)

        ShowAll= Button(Buttonframe, command=self.fetch_data ,width=15, text="Show all", font=("Times New Roman", 12,'bold'), bg= "teal", fg="white")
        ShowAll.grid(row=0, column=9)



        #--------dataframe left-----------
        #--- label and entry---
        lblRefno = Label(DataframeLeft, text="Reference No", font=("Times New Roman", 13, 'bold'), padx=2, pady=0)
        lblRefno.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="pharma"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Ref FROM pharma_med")
        rows = my_cursor.fetchall()
        ref_list = [row[0] for row in rows]  # Flatten the list of tuples
        ref_combo = ttk.Combobox(DataframeLeft, textvariable=self.refv, width=16, font=("Times New Roman", 14, 'bold'), state="readonly")
        ref_combo["values"] = ref_list
        ref_combo.grid(row=0, column=1, pady=2)
        ref_combo.current(0)

        lblCompName = Label(DataframeLeft, text="Company Name:", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblCompName.grid(row=1, column=0, sticky=W)
        txtCompName = Entry(DataframeLeft, textvariable=self.compNamev, bd=3, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtCompName.grid(row=1, column=1, pady=3)

        lblType = Label(DataframeLeft, text="Type Of Medicine:", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblType.grid(row=2, column=0, sticky=W)
        type_combo = ttk.Combobox(DataframeLeft, textvariable=self.typeMedv, width=16, font=("Times New Roman", 14, 'bold'), state="readonly")
        type_combo["values"] = ("Tablet", "Liquid", "Capsules", "Topical Medicines", "Drops", "Inhales", "Injections")
        type_combo.grid(row=2, column=1, pady=3)
        type_combo.current(0)

        lblLotno = Label(DataframeLeft, text="Lot No.", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblLotno.grid(row=3, column=0, sticky=W)
        txtlot = Entry(DataframeLeft, textvariable=self.lotv, bd=3, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtlot.grid(row=3, column=1, pady=3)

        lblIssueDate = Label(DataframeLeft, text="Issue Date:", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblIssueDate.grid(row=4, column=0, sticky=W)
        txtiss = Entry(DataframeLeft, textvariable=self.issueDatev, bd=3, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtiss.grid(row=4, column=1, pady=3)

        lblExpDate = Label(DataframeLeft, text="Exp Date:", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblExpDate.grid(row=5, column=0, sticky=W)
        txtexp = Entry(DataframeLeft, textvariable=self.expDatev, bd=3, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtexp.grid(row=5, column=1, pady=3)

        lblUse = Label(DataframeLeft, text="Uses:", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblUse.grid(row=6, column=0, sticky=W)
        txtuse = Entry(DataframeLeft, bd=3, textvariable=self.usesv, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtuse.grid(row=6, column=1, pady=3)

        lblSideEff = Label(DataframeLeft, text="Side Effects:", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblSideEff.grid(row=7, column=0, sticky=W)
        txtse = Entry(DataframeLeft, bd=3, textvariable=self.sideeffectv, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtse.grid(row=7, column=1, pady=3)

        lblMedName = Label(DataframeLeft, text="Medicine Name", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblMedName.grid(row=8, column=0, sticky=W)

        my_cursor.execute("SELECT MedName FROM pharma_med")
        med_rows = my_cursor.fetchall()
        med_list = [row[0] for row in med_rows]  # Flatten the list of tuples
        Medname_combo = ttk.Combobox(DataframeLeft, textvariable=self.medNamev, width=16, font=("Times New Roman", 14, 'bold'), state="readonly")
        Medname_combo["values"] = med_list
        Medname_combo.grid(row=8, column=1, pady=3)
        Medname_combo.current(0)

        lblPnW = Label(DataframeLeft, text="     Prec&Warning", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblPnW.grid(row=0, column=2, sticky=W)
        txtpnw = Entry(DataframeLeft, bd=3, textvariable=self.warningv, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtpnw.grid(row=0, column=3, pady=4)

        lblDosage = Label(DataframeLeft, text="     Dosage", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtDosage = Entry(DataframeLeft, bd=3, textvariable=self.dosagev, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtDosage.grid(row=1, column=3, pady=4)

        lblTblPrice = Label(DataframeLeft, text="     Tablet Price", font=("Times New Roman", 13, 'bold'), padx=2, pady=3)
        lblTblPrice.grid(row=2, column=2, sticky=W)
        txtprice = Entry(DataframeLeft, bd=3, textvariable=self.pricev, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtprice.grid(row=2, column=3, pady=4)

        lblProQt = Label(DataframeLeft, text="     Product Qt:", font=("Times New Roman", 13, 'bold'), padx=5, pady=3)
        lblProQt.grid(row=3, column=2, sticky=W)
        txtproqt = Entry(DataframeLeft, textvariable=self.productqtv, bd=3, relief=RIDGE, font=("Times New Roman", 13, 'bold'))
        txtproqt.grid(row=3, column=3, pady=4)

        conn.close()



        #-----images----
        lblText= Label(DataframeLeft, text="Stay Healthy Stay Safe", font=("Times New Roman", 11,'bold'),padx=15,pady=2, bg= 'white', fg= 'Green', width= 42)
        lblText.place(x=343, y= 140)

        img2= Image.open("D:\\pharma prjt_sql&py\\2.jpg") #use \\ not \
        img2= img2.resize((136,135), Image.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)
        b1= Button(self.root, image=self.photoimg2, borderwidth=0)
        b1.place(x=400, y=310)

        img3= Image.open("D:\\pharma prjt_sql&py\\1.jpg") #use \\ not \
        img3= img3.resize((136,135), Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)
        b1= Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=536, y=310)

        img4= Image.open("D:\\pharma prjt_sql&py\\4.jpg") #use \\ not \
        img4= img4.resize((136,135), Image.LANCZOS)
        self.photoimg4= ImageTk.PhotoImage(img4)
        b1= Button(self.root, image=self.photoimg4, borderwidth=0)
        b1.place(x=672, y=310)   

        
        #-----------datafram right----------
        img5= Image.open("D:\\pharma prjt_sql&py\\33.jpg") #use \\ not \
        img5= img5.resize((120,110), Image.LANCZOS)
        self.photoimg5= ImageTk.PhotoImage(img5)
        b1= Button(self.root, image=self.photoimg5, borderwidth=0)
        b1.place(x=870, y=140)

        img6= Image.open("D:\\pharma prjt_sql&py\\5.jpg") #use \\ not \
        img6= img6.resize((120,110), Image.LANCZOS)
        self.photoimg6= ImageTk.PhotoImage(img6)
        b1= Button(self.root, image=self.photoimg6, borderwidth=0)
        b1.place(x=990, y=140)

        img7= Image.open("D:\\pharma prjt_sql&py\\6.jpg") #use \\ not \
        img7= img7.resize((120,110), Image.LANCZOS)
        self.photoimg7= ImageTk.PhotoImage(img7)
        b1= Button(self.root, image=self.photoimg7, borderwidth=0)
        b1.place(x=1110,y=140)

        lblRefnoo= Label(DataframeRight,  text="Reference No. :", font=("Times New Roman", 13,'bold'))
        lblRefnoo.place(x=0, y=110)
        txtRefnoo= Entry(DataframeRight, textvariable= self.ref_var,  font=("Times New Roman", 12,'bold'), bg= 'white', bd=2, relief=RIDGE, width=12)
        txtRefnoo.place(x=135, y=110)

        lblRefnoo= Label(DataframeRight,  text="Medicine Name :", font=("Times New Roman", 13,'bold'))
        lblRefnoo.place(x=0, y=140)
        txtmedName= Entry(DataframeRight, textvariable= self.addmed_var,  font=("Times New Roman", 12,'bold'), bg= 'white', bd=2, relief=RIDGE, width=12)
        txtmedName.place(x=135, y=140)
        conn.close()

        #--- right side frame new---
        side_frame= Frame(DataframeRight, bd=4, relief=RIDGE, bg='white')
        side_frame.place(x=0, y=175, width=240, height=120)

        sc_x= ttk.Scrollbar(side_frame, orient= HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y= ttk.Scrollbar(side_frame, orient= VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table= ttk.Treeview(side_frame, column=("ref", "medname"), xscrollcommand= sc_x.set,yscrollcommand= sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text= "Ref")
        self.medicine_table.heading("medname", text= "Medicine Name")

        self.medicine_table['show']= "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)

        #----- medicine add btn----------
        down_frame= Frame(DataframeRight, bd=4, relief=RIDGE, bg="lavender", padx=2, pady=5)
        down_frame.place(x=250, y=112, width=95, height=178)

        #button add karre hai ab
        btnAddMed= Button(down_frame, width=8,text="ADD", font=("Times New Roman", 11,'bold'), bg= "#AFEEEE", fg="black", pady=6 , padx=2, command=self.Addmed)
        btnAddMed.grid(row=0, column=0)

        btnUpdMed= Button(down_frame, width=8,text="UPDATE", font=("Times New Roman", 11,'bold'), bg= "#F0E68C", fg="black", pady=6 , padx=2,  command=self.UpdateMed)
        btnUpdMed.grid(row=1, column=0)

        btnDelMed= Button(down_frame, width=8,text="DELETE", font=("Times New Roman", 11,'bold'), bg= "#FF6666", fg="black", pady=6 , padx=2, command=self.DeleteMed)
        btnDelMed.grid(row=2, column=0)

        btnClearMed= Button(down_frame, width=8,text="CLEAR", font=("Times New Roman", 11,'bold'), bg= "light green", fg="black", pady=6 , padx=2, command=self.ClearMed)
        btnClearMed.grid(row=3, column=0)


        #------- frame details------
        frame_details= Frame(self.root, bd=6, relief=RIDGE, bg="lavender")
        frame_details.place(x=0, y=520, width=1280, height=127)


        #---main table and scroll bar----

        table_frame= Frame(self.root, bd=5, relief=RIDGE)
        table_frame.place(x=1, y=525, width=1275, height= 117)



        scr_x= ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scr_x.pack(side=BOTTOM, fill=X)
        scr_y= ttk.Scrollbar(table_frame, orient= VERTICAL)
        scr_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table= ttk.Treeview(table_frame, columns=('Refno', 'companyname', 'type', 'medname', 'lot', 'issuedate', 'expdate', 'uses', 'sideeffect', 'warning', 'dosage', 'price', 'productqt'), xscrollcommand=scr_x.set, yscrollcommand=scr_y.set)

        self.pharmacy_table['show']= "headings"
        
        self.pharmacy_table.heading('Refno', text="Reference no.")
        self.pharmacy_table.heading('companyname', text="Company Name")
        self.pharmacy_table.heading('type', text="Type of Medicine")
        self.pharmacy_table.heading('medname', text="Medame")
        self.pharmacy_table.heading('lot', text="Lot no.")
        self.pharmacy_table.heading('issuedate', text="Issue Date")
        self.pharmacy_table.heading('expdate', text="Expiry Date")
        self.pharmacy_table.heading('uses', text="Uses")
        self.pharmacy_table.heading('sideeffect', text="Side effects")
        self.pharmacy_table.heading('warning', text="Warnings")
        self.pharmacy_table.heading('dosage', text="Dosage")
        self.pharmacy_table.heading('price', text="Price")
        self.pharmacy_table.heading('productqt', text="Product QT")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("Refno", width=100)
        self.pharmacy_table.column("companyname", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("medname", width=100)
        self.pharmacy_table.column("lot", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideeffect", width=100)
        self.pharmacy_table.column("warning", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqt", width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)



        #-----Add med functionality declaration----
    def Addmed(self):
           
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pharma"
            )
        my_cursor = conn.cursor()
        my_cursor.execute("INSERT INTO pharma_med (ref, medname) VALUES (%s, %s)", (
                self.ref_var.get(),
                self.addmed_var.get()
            ))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success", "Medicine added successfully")
            
                

    def fetch_dataMed(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pharma"
            )
        my_cursor= conn.cursor()
        my_cursor.execute("SELECT * FROM pharma_med")
        rows= my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def Medget_cursor(self, event=""):
        cursor_row= self.medicine_table.focus()
        content= self.medicine_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0])
        self.addmed_var.set(row[1])
    

    #---update decl----
    def UpdateMed(self):
        if self.ref_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pharma"
            )
            my_cursor= conn.cursor()
            my_cursor.execute("update pharma_med set MedName=%s where Ref=%s", (self.addmed_var.get() ,self.ref_var.get(),))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been Updated")

    def DeleteMed(self):
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pharma"
            )
            my_cursor= conn.cursor()
            sql="delete from pharma_med where Ref=%s"
            val=(self.ref_var.get(),)
            my_cursor.execute(sql,val)
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been Deleted")


    def ClearMed(self):
            self.ref_var.set("")
            self.addmed_var.set("")
            messagebox.showinfo("Success", "Medicine has been Cleared")


    #----------- main table----------
    def add_data(self):
        if self.refv.get() == "" or self.lotv.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="pharma"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    INSERT INTO pharmacy (Ref, compName, typeMed, medName,Lot, issueDate ,expDate ,uses ,sideeffect , warning ,dosage,price ,productqt ) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.refv.get(),
                    self.compNamev.get(),
                    self.typeMedv.get(),
                    self.medNamev.get(),
                    self.lotv.get(),                                    
                    self.issueDatev.get(),
                    self.expDatev.get(),
                    self.usesv.get(),  
                    self.sideeffectv.get(),
                    self.warningv.get(),
                    self.dosagev.get(),
                    self.pricev.get(),
                    self.productqtv.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data has been inserted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
            finally:
                if conn.is_connected():
                    conn.close()


    def fetch_data (self):
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="pharma"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy")
        row=my_cursor.fetchall()
        if len(row) !=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    
    def get_cursor(self, ev=""):
        cursor_row= self.pharmacy_table.focus()
        content= self.pharmacy_table.item(cursor_row)
        row=content["values"]
        self.refv.set(row[0]),
        self.compNamev.set(row[1]),
        self.typeMedv.set(row[2]),
        self.medNamev.set(row[3]),
        self.lotv.set(row[4]),                                    
        self.issueDatev.set(row[5]),
        self.expDatev.set(row[6]),
        self.usesv.set(row[7]),  
        self.sideeffectv.set(row[8]),            
        self.warningv.set(row[9]),
        self.dosagev.set(row[10]),
        self.pricev.set(row[11]),
        self.productqtv.set(row[12])

    def Update(self):
        if self.refv.get()=="" or self.lotv.get()=="":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pharma"
            )
            my_cursor= conn.cursor()
            my_cursor.execute("update pharmacy set compName=%s, typeMed=%s,medName=%s,Lot=%s, issueDate=%s, expDate=%s, uses=%s, sideeffect=%s, warning=%s,dosage=%s,price=%s, productqt=%s where Ref=%s", (self.compNamev.get(),
                    self.typeMedv.get(),
                    self.medNamev.get(),
                    self.lotv.get(),                                    
                    self.issueDatev.get(),
                    self.expDatev.get(),
                    self.usesv.get(),  
                    self.sideeffectv.get(),                        
                    self.warningv.get(),
                    self.dosagev.get(),
                    self.pricev.get(),
                    self.productqtv.get(), self.refv.get()
                    ))
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been Updated")

    def Delete(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pharma"
            )
        my_cursor= conn.cursor()
        sql="delete from pharmacy where Ref=%s"
        val=(self.refv.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Medicine has been Deleted")

    def Clear(self):
        #self.refv.set("")
        self.compNamev.set(""),
        #self.typeMedv.set(""),
        self.lotv.set(""),                                    
        self.issueDatev.set(""),
        self.expDatev.set(""),
        self.usesv.set(""),  
        self.sideeffectv.set(""),
        #self.medNamev.set(""),    
        self.warningv.set(""),
        self.dosagev.set(r""),
        self.pricev.set(r""),
        self.productqtv.set(r"")
        messagebox.showinfo("Success", "Medicine has been Reseted")


    
    def search_data(self):
        search_term = self.searchtxt_var.get()  # Get search term
        search_column = self.search_var.get()  # Get search column

        if search_term and search_column != "Choose:":
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="pharma"
                )
                my_cursor = conn.cursor()

                # Use parameterized query to prevent SQL injection
                query = "SELECT * FROM pharmacy WHERE " + search_column + " LIKE %s"
                my_cursor.execute(query, (search_term,))  # Use tuple for parameters

                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                    for row in rows:
                        self.pharmacy_table.insert("", END, values=row)
                conn.commit()

            except mysql.connector.Error as err:
                # Handle database connection error
                messagebox.showerror("Error", "Database connection error: " + str(err))
            finally:
                # Close connection if it was opened (even in case of errors)
                if conn:
                    conn.close()
        else:
            # Handle case where no search term or column is selected
            messagebox.showerror("Error", "Please select a search column and enter a search term.")

                


if __name__== "__main__":
    root= Tk()
    obj= PharmacyManagementSystem(root)
    root.mainloop()