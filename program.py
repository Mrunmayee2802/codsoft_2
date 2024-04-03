import tkinter
import tkMessageBox
top=tkinter.Tk()
def hellomsg():
    tkMessageBox.showinfo("hello")

B1=tkinter.Button(top,text="first",command=hellomsg())
B2=tkinter.Button(top,text="second")
B1.pack()
B2.pack()
top.mainloop()
