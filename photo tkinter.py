from tkinter import *
wind = Tk()
wind.geometry('400x300')
wind.config(bg="dodger blue")
my_image = PhotoImage(file= "C:/Users/020281/bookshelf.gif")
lbl = Label(image=my_image).pack()
wind.mainloop()
