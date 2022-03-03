from tkinter import *
from turtle import width
root = Tk()

def send():
    send="You =>>"+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
         txt.insert(END,"\n"+"Bot =>> Hi")
    elif(e.get()=="hi"):
         txt.insert(END,"\n"+"Bot =>> Hello")
    elif(e.get()=="What are you doing?"):
         txt.insert(END,"\n"+"Bot =>> Replying You....")
    elif(e.get()=="How Are You.."):
         txt.insert(END,"\n"+"Bot =>> Fine.You?")
    elif(e.get()=="Good Morning"):
         txt.insert(END,"\n"+"Bot =>> GM..")
    else:
         txt.insert(END,"\n"+"Bot =>> Sorry I didn't get it (-_-)....!")
        
    e.delete(0,END)

txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("ChatBot")
root.mainloop()