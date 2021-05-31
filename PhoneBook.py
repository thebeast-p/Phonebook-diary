import MySplash

import sqlite3
con=sqlite3.Connection('hrdb3')
cur=con.cursor()

# image in Tkinter
# gif
from tkinter import *

root=Tk()
root.geometry('750x850')
root.title(" My PhoneBook ")
root.config(bg='lightsteelblue')
img= PhotoImage(file='image2.gif')
Button(root,image=img).grid(row= 0,column=1)

# DataBase Table

cur.execute('create table if not exists CInfo(ContactID integer primary key autoincrement,fname varchar(20),mname varchar(20),lname varchar(20),Company varchar(30),Address varchar(50),City varchar(30),Pin number , Website varchar(50),dob date)')
cur.execute('create table if not exists PhInfo(ContactID integer primary key autoincrement,Contact_Type varchar(20),PhNo number,foreign key(ContactID) references CInfo(ContactID))')
cur.execute('create table if not exists MailInfo(ContactID integer primary key autoincrement,Email_Type varchar(50),EmailID varchar(50),foreign key(ContactID) references CInfo(ContactID))')

#GUI

Label(root,text=" First Name : ",font='bold',bg='lightsteelblue').grid(row= 1,column=0 )
a=Entry(root)
a.grid(row= 1,column= 1)

Label(root,text=" Middle Name : ",font='bold',bg='lightsteelblue').grid(row= 2,column=0 )
b=Entry(root)
b.grid(row= 2,column= 1)

Label(root,text=" Last Name : ",font='bold',bg='lightsteelblue').grid(row= 3,column=0 )
c=Entry(root)
c.grid(row= 3,column= 1)

Label(root,text="  Company Name : ",font='bold',bg='lightsteelblue').grid(row= 4,column=0 )
d=Entry(root)
d.grid(row= 4,column= 1)

Label(root,text=" Address : ",font='bold',bg='lightsteelblue').grid(row= 5,column=0 )
e=Entry(root)
e.grid(row= 5,column= 1)

Label(root,text=" City : ",font='bold',bg='lightsteelblue').grid(row= 6,column=0 )
f=Entry(root)
f.grid(row= 6,column= 1)

Label(root,text=" Pin Code : ",font='bold',bg='lightsteelblue').grid(row= 7,column=0 )
g=Entry(root)
g.grid(row= 7,column= 1)

Label(root,text=" Websity URL : ",font='bold',bg='lightsteelblue').grid(row= 8,column=0 )
h=Entry(root)
h.grid(row= 8,column= 1)

Label(root,text=" Date of Birth : ",font='bold',bg='lightsteelblue').grid(row= 9,column= 0)
i=Entry(root)
i.grid(row= 9,column= 1)

Label(root,text=" Select Phone type : ",fg='blue',font='bold',bg='lightsteelblue').grid(row= 10,column= 0)
v1=IntVar()
u=Radiobutton(root,text=' Office ',bg='lightsteelblue',variable=v1,value=1)
u.grid(row= 10,column= 1)
v=Radiobutton(root,text=' Home ',bg='lightsteelblue',variable=v1,value=2)
v.grid(row= 10,column= 2)
w=Radiobutton(root,text=' Mobile ',bg='lightsteelblue',variable=v1,value=3)
w.grid(row= 10,column= 3)
Label(root,text=" Phone Number : ",font='bold',bg='lightsteelblue').grid(row= 11,column=0 )
x=Entry(root)
x.grid(row= 11,column= 1)

Label(root,text=" Select Email Type ",fg='blue',font='bold',bg='lightsteelblue').grid(row= 12,column= 0)
v2=IntVar()
y=Radiobutton(root,text=' Office ',bg='lightsteelblue',variable=v2,value=1)
y.grid(row= 12,column= 1)
z=Radiobutton(root,text=' Personal ',bg='lightsteelblue',variable=v2,value=2)
z.grid(row= 12,column= 2)
Label(root,text=" Email id : ",font='bold',bg='lightsteelblue').grid(row= 13,column=0 )
p=Entry(root)
p.grid(row= 13,column= 1)


def close2(e = 1):
    root.destroy()

#import tkMessageBox

def save():
    cur.execute("insert into CInfo(fname ,mname,lname ,Company,Address ,City ,Pin , Website ,dob)values (?,?,?,?,?,?,?,?,?)",(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get(),i.get()))
    cur.execute("insert into PhInfo(Contact_Type ,PhNo)values (?,?)",(v1.get(),x.get()))
    cur.execute("insert into MailInfo(Email_Type,EmailID)values (?,?)",(v2.get(),p.get()))
    con.commit()

    a.delete(0,END)
    b.delete(0,END)
    c.delete(0,END)
    d.delete(0,END)
    e.delete(0,END)
    f.delete(0,END)
    g.delete(0,END)
    h.delete(0,END)
    i.delete(0,END)

    x.delete(0,END)
    p.delete(0,END)
    
    tkMessageBox.showinfo("SaveWindow","Save Successful!!!")
    
def search():
    root1=Tk()
    root1.geometry("750x1000")
    root1.title('Search')
    root1.configure(bg="gray")
    Label(root1,text="Search",font="Times 22 bold",bg="gray").grid(row=0,column=0)
    Label(root1,text="Enter The Name",font="Arial 15 bold",bg="gray").grid(row=3,column=3)
    z1=Entry(root1,bd=3)
    z1.grid(row=4,column=3)
    lb1=Listbox(root1,bd=3,height=17,width=40,selectmode=SINGLE,bg="White",font="Arial 18 bold")
    lb1.grid(row=5,column=2,columnspan=3)


    def searching(u=1):
        lb1.delete(0,END)
        t=["%"+z1.get()+"%","%"+z1.get()+"%","%"+z1.get()+"%"]
        cur.execute("SELECT fname,mname,lname FROM CInfo WHERE fname LIKE ? OR mname LIKE ? OR lname LIKE ? ",t)
        t=cur.fetchall()
        for i in t:
            k=i[0]+' '+i[1]+' '+i[2]
            print (k)
            lb1.insert(END,k)
    root1.bind('<KeyPress>',searching)
    
    def fetch():
        root2=Tk()
        lb2=Listbox(root2,bd=3,height=17,width=40,font="Arial 14 bold")
        lb2.pack()
        a= lb1.curselection()
        x=lb1.get(a)
        x=x.split(' ')
        cur.execute("SELECT * FROM CInfo WHERE fname=? AND mname=? AND lname=?",x)
        T=cur.fetchall()
        
        for i in T:
            print (T,'\n')
            a="fname :  "+i[1]
            lb2.insert(END,a)
            a="mname: "+i[2]
            lb2.insert(END,a)
            a="lname :  "+i[3]
            lb2.insert(END,a)
            a="comp_name :  "+i[4]
            lb2.insert(END,a)
            a="address :  "+i[5]
            lb2.insert(END,a)
            a="city :  "+i[6]
            lb2.insert(END,a)
            x=str(i[7])
            a="pin :  "+x
            lb2.insert(END,a)
            a="web :  "+i[8]
            lb2.insert(END,a)
        cur.execute("SELECT PhNo FROM PhInfo WHERE ContactId=?",str(T[0][0]))
        x=cur.fetchall()
        a="phone :  ",x
        lb2.insert(END,a)
        cur.execute("SELECT EmailID FROM MailInfo WHERE ContactId=?",str(T[0][0]))
        x=cur.fetchall()
        #print x
        a="email : "+x[0][0]
        lb2.insert(END,a)

    def close():
         root1.destroy() 
    Button(root1,text="CLOSE",command=close).grid(row=20,column=4)
    def delete():
        
            a= lb1.curselection()
            x=lb1.get(a)
            x=x.split(' ')
            cur.execute("DELETE FROM CInfo WHERE fname=? AND mname=? AND lname=?",x)
            con.commit()
            tkMessageBox.showinfo("Contact Delete","Contact has been deleted")
            root1.destroy()
    
    Button(root1, text="Delete",command=delete).grid(row=20,column=3)
    lb1.bind('<Double-Button-1>', lambda x:fetch())
    Button(root1,text="CLOSE",command=close).grid(row=20,column=4)
    con.commit()


def close():
    root.destroy()
    
    

#root.bind('<KeyPress>', close2)


Button(root,text = " Save ",command=save).grid(row= 14,column= 0)


Button(root,text = " Search ",command=search).grid(row= 14,column= 1)

Button(root,text = " Close ",command=close).grid(row= 14,column= 2)



root.mainloop()








