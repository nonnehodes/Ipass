from tkinter import *
import webbrowser

root = Tk()
root.title('Floorball voorspelling')

# ------------------------------------------------------------------------------------------------------------------#
# kleine functies #

def openWebsite(url):
    webbrowser.open(url)

# ------------------------------------------------------------------------------------------------------------------#
# Achtergrond #

C = Canvas(root, height=605, width=891)
filename = PhotoImage(file="Floorballveld.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# ------------------------------------------------------------------------------------------------------------------#
# Frames #

frame1 = Frame(root, bg="#f5faff")
frame1.place(relx=0.15, rely=0.1, relwidth=0.6, relheight=0.5)

frame2 = Frame(root, bg="#f5faff")
frame2.place(relx=0.2, rely=0.65, relwidth=0.5, relheight=0.25)

# ------------------------------------------------------------------------------------------------------------------#
# Labels #

uitslag = Label(master=frame2, text='Uitslag', height=1, bg="#f5faff", fg="#004080")
uitslag.config(font=("Britannic bold", 25))
uitslag.pack()

# ------------------------------------------------------------------------------------------------------------------#
# buttons #

voorspelKnop = Button(master=frame1, text='Voorspel', bg="#f5faff", fg="#004080")
voorspelKnop.config(font=("Britannic bold", 20))
voorspelKnop.place(x=205, y=220)

NeFUBKnop = Button(master=root, text='NeFUB site', bg="#b3cce6", fg="#004080")
NeFUBKnop.config(font=("Calibri light", 10))
NeFUBKnop.place(x=738, y=195)
NeFUBKnop.bind("<Button-1>", lambda e: openWebsite("https://nefub.nl/floorball/"))

HUKnop = Button(master=root, text='HU site', bg="#b3cce6", fg="#004080")
HUKnop.config(font=("Calibri light", 10))
HUKnop.place(x=747, y=383)
HUKnop.bind("<Button-1>", lambda e: openWebsite("https://www.hu.nl/"))

# ------------------------------------------------------------------------------------------------------------------#
# optie menu's' #
teamLijst = ["utrecht 1", "utrecht 2", "Sonics"]
scheidsLijst = ["1", "2", "3", "4"]

variableThuisTeam = StringVar(frame1)
variableThuisTeam.set("Thuis team")
optiesThuisTeam = OptionMenu(frame1, variableThuisTeam, *teamLijst)
optiesThuisTeam.config(font=("Britannic bold", 30), bg="#f5faff", fg="#004080")
optiesThuisTeam.place(x=10, y=20, height=70, width=245)

variableUitTeam = StringVar(frame1)
variableUitTeam.set("Uit team")
optiesUitTeam = OptionMenu(frame1, variableUitTeam, *teamLijst)
optiesUitTeam.config(font=("Britannic bold", 30), bg="#f5faff", fg="#004080")
optiesUitTeam.place(x=280, y=20, height=70, width=245)

variableScheids1= StringVar(frame1)
variableScheids1.set("Scheidsrechter 1")
optiesScheids1 = OptionMenu(frame1, variableScheids1, *scheidsLijst)
optiesScheids1.config(font=("Britannic bold", 18), bg="#f5faff", fg="#004080")
optiesScheids1.place(x=10, y=130, height=60, width=245)

variableScheids2= StringVar(frame1)
variableScheids2.set("Scheidsrechter 2")
optiesScheids2 = OptionMenu(frame1, variableScheids2, *scheidsLijst)
optiesScheids2.config(font=("Britannic bold", 18), bg="#f5faff", fg="#004080")
optiesScheids2.place(x=280, y=130, height=60, width=245)


# ------------------------------------------------------------------------------------------------------------------#

root.mainloop()

# ------------------------------------------------------------------------------------------------------------------#
# Bronnen #

# https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
# https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter
# https://canvas.hu.nl/courses/12972/assignments/43477?module_item_id=162145
# https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter






# ------------------------------------------------------------------------------------------------------------------#
############### ongebruikte code ###############
# ------------------------------------------------------------------------------------------------------------------#
# Labels #

# thuisClub = Label(master=frame1, text='Thuis Club', height=2, bg="#f5faff", fg="#004080")
# thuisClub.config(font=("Britannic bold", 20))
# thuisClub.place(x=20, y=0)
#
# thuisTeam = Label(master=frame1, text='Team', height=2, bg="#f5faff", fg="#004080")
# thuisTeam.config(font=("Britannic bold", 20))
# thuisTeam.place(x=185, y=0)
#
# uitClub = Label(master=frame1, text='Uit Club', height=2, bg="#f5faff", fg="#004080")
# uitClub.config(font=("Britannic bold", 20))
# uitClub.place(x=285, y=0)
#
# uitTeam = Label(master=frame1, text='Team', height=2, bg="#f5faff", fg="#004080")
# uitTeam.config(font=("Britannic bold", 20))
# uitTeam.place(x=450, y=0)

# scheids1 = Label(master=frame1, text='Scheidsrechter 1', height=2, bg="#f5faff", fg="#004080")
# scheids1.config(font=("Britannic bold", 17))
# scheids1.place(x=20, y=110)
#
# scheids2 = Label(master=frame1, text='Scheidsrechter 2', height=2, bg="#f5faff", fg="#004080")
# scheids2.config(font=("Britannic bold", 17))
# scheids2.place(x=335, y=110)

# ------------------------------------------------------------------------------------------------------------------#
# entry's #

#inputThuisClub = Entry(master=frame1)
#inputThuisClub.config(font=("Calibri", 15))
#inputThuisClub.place(x=20, y=60, height=40, width=150)

#inputThuisTeam = Entry(master=frame1)
#inputThuisTeam.config(font=("Calibri", 15))
#inputThuisTeam.place(x=185, y=60, height=40, width=70)

#inputUitClub = Entry(master=frame1)
#inputUitClub.config(font=("Calibri", 15))
#inputUitClub.place(x=285, y=60, height=40, width=150)

#inputUitTeam = Entry(master=frame1)
#inputUitTeam.config(font=("Calibri", 15))
#inputUitTeam.place(x=450, y=60, height=40, width=70)

# inputScheids1 = Entry(master=frame1)
# inputScheids1.config(font=("Calibri", 15))
# inputScheids1.place(x=20, y=160, height=40, width=235)
#
# inputScheids2 = Entry(master=frame1)
# inputScheids2.config(font=("Calibri", 15))
# inputScheids2.place(x=285, y=160, height=40, width=235)