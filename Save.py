def save():
    cur.execute("insert into PB_1(First_Name ,Middle_Name,Last_Name ,Company,Address ,City ,Pin , Website ,Birth_Date)values (?,?,?,?,?,?,?,?,?)",(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get(),i.get()))
    cur.execute("insert into PB_2(Contact_Type ,Phone_number)values (?,?)",(v1.get(),x.get()))
    cur.execute("insert into PB_3(Email_Type,EmailID)values (?,?)",(v2.get(),p.get()))
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

