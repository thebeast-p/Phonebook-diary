from tkinter import *

root=Tk()
root.geometry('750x150')
root.title("MySplash")
root.config(bg='whitesmoke')
Label(root,text="PHONEBOOK",font='times 30 bold',bg='whitesmoke',fg='royalblue1').grid(row= 0,column=0)
Label(root,text="Project of Python and Database",font='times 15 bold',bg='whitesmoke',fg='royalblue1').grid(row= 1,column=1)
Label(root,text="Developed By: Prabal Asthana(181B147)",font='times 15 bold',bg='whitesmoke',fg='royalblue1').grid(row= 2,column=1)
Label(root,text="MOVE MOUSE POINTER TO EXIT THIS SCREEN",font='times 8 bold',bg='whitesmoke',fg='royalblue1').grid(row= 3,column=1)
def close(t=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()
