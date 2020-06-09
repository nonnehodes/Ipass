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
# Labels en entry's frame 1 #

label1 = Label(master=frame1, text='Thuis team', height=2, bg="#f5faff", fg="#004080")
label1.config(font=("Britannic bold", 20))
label1.place(x=20, y=0)

entry1 = Entry(master=frame1)
entry1.config(font=("Calibri", 15))
entry1.place(x=20, y=60, height=40, width=230)

label2 = Label(master=frame1, text='Uit team', height=2, bg="#f5faff", fg="#004080")
label2.config(font=("Britannic bold", 20))
label2.place(x=405, y=0)

entry2 = Entry(master=frame1)
entry2.config(font=("Calibri", 15))
entry2.place(x=285, y=60, height=40, width=230)

label3 = Label(master=frame1, text='Scheidsrechter 1', height=2, bg="#f5faff", fg="#004080")
label3.config(font=("Britannic bold", 17))
label3.place(x=20, y=110)

entry3 = Entry(master=frame1)
entry3.config(font=("Calibri", 15))
entry3.place(x=20, y=160, height=40, width=230)

label4 = Label(master=frame1, text='Scheidsrechter 2', height=2, bg="#f5faff", fg="#004080")
label4.config(font=("Britannic bold", 17))
label4.place(x=335, y=110)

entry4 = Entry(master=frame1)
entry4.config(font=("Calibri", 15))
entry4.place(x=285, y=160, height=40, width=230)

#------------------------------------------------------------------------------------------------------------------#
# Labels frame 2 #

label5 = Label(master=frame2, text='Uitslag', height=1, bg="#f5faff", fg="#004080")
label5.config(font=("Britannic bold", 25))
label5.pack()

#------------------------------------------------------------------------------------------------------------------#
# buttons #

button1 = Button(master=frame1, text='Voorspel', bg="#f5faff", fg="#004080")
button1.config(font=("Britannic bold", 15))
button1.place(x=220, y=230)

button2 = Button(master=root, text='NeFUB site', bg="#b3cce6", fg="#004080")
button2.config(font=("Calibri light", 10))
button2.place(x=738, y=195)

button3 = Button(master=root, text='HU site', bg="#b3cce6", fg="#004080")
button3.config(font=("Calibri light", 10))
button3.place(x=747, y=383)

#------------------------------------------------------------------------------------------------------------------#


root.mainloop()