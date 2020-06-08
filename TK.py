from tkinter import *

root = Tk()
root.title('Floorball voorspelling')

#------------------------------------------------------------------------------------------------------------------#
# Achtergrond #

C = Canvas(root, height=605, width=891)
filename = PhotoImage(file = "Floorballveld.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

#------------------------------------------------------------------------------------------------------------------#
# Frames #

frame1 = Frame(root, bg="#f5faff")
frame1.place(relx=0.15, rely=0.1, relwidth=0.6, relheight=0.5)

frame2 = Frame(root, bg="#f5faff")
frame2.place(relx=0.2, rely=0.65, relwidth=0.5, relheight=0.25)

#------------------------------------------------------------------------------------------------------------------#
# Labels #

label1 = Label(master=root, text='thuis team', height=2)
label1.pack()

root.mainloop()