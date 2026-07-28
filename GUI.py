from tkinter import *

window = Tk()

photo = PhotoImage(file='C:\\Users\\USER\\Downloads\\GOAT.png')

label = Label(window,
              text="Hello",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()

window.geometry("420x420")
window.title("Piyarul first GUI Program")

window.config(background="#d8d0c8")

window.mainloop()