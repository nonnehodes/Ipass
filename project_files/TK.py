from tkinter import *
import webbrowser
from tkinter import messagebox

from project_files.algorithms.AlgorithmDecisionTree import AlgorithmDecisionTree
from project_files.algorithms.AlgorithmLinRegress import AlgorithmLinRegress
from project_files.algorithms.AlgorithmMLR import AlgorithmMLR
from project_files.helpers import create_superteams_list, create_club_objects
from project_files.database.load_data import get_clubnames, get_team_score, get_locaties, get_scheidsrechters

root = Tk()
root.title('Floorball voorspelling')

hometeam = ''
awayteam = ''
ref1 = ''
ref2 = ''
algorithm = ''
location = ''
# ------------------------------------------------------------------------------------------------------------------#
# kleine functies #

def openWebsite(url):
    webbrowser.open(url)

def set_hometeam(value):
    global hometeam
    hometeam = value
    build_scheidsrechters_dropdown(hometeam, awayteam)


def set_awayteam(value):
    global awayteam
    awayteam = value
    build_scheidsrechters_dropdown(hometeam, awayteam)


def build_scheidsrechters_dropdown(hometeam, awayteam):
    if hometeam != '' and awayteam != '':
        for club in clubs:
            if club.get_clubnaam() in hometeam:
                home_teams = club.get_superteams()[hometeam]

            if club.get_clubnaam() in awayteam:
                away_teams = club.get_superteams()[awayteam]

        home_refs = get_scheidsrechters(home_teams, away_teams)
        away_refs = get_scheidsrechters(away_teams, home_teams)

        refs_list = list(set(home_refs) | set(away_refs))
        variableRef1 = StringVar(frame1)
        variableRef1.set("Scheidsrechter 1")
        optionsRef1 = OptionMenu(frame1, variableRef1, *refs_list, command=set_ref1)
        optionsRef1.config(font=("Britannic bold", 18), bg="#f5faff", fg="#004080")
        optionsRef1.place(x=10, y=100, height=60, width=245)

        variableRef2 = StringVar(frame1)
        variableRef2.set("Scheidsrechter 2")
        optionsRef2 = OptionMenu(frame1, variableRef2, *refs_list, command=set_ref2)
        optionsRef2.config(font=("Britannic bold", 18), bg="#f5faff", fg="#004080")
        optionsRef2.place(x=280, y=100, height=60, width=245)

        home_locations = get_locaties(home_teams, away_teams)
        away_locations = get_locaties(away_teams, home_teams)
        location_list =  list(set(home_locations) & set(away_locations))

        variableLocation = StringVar(frame1)
        variableLocation.set("Locatie")
        optionsLocation = OptionMenu(frame1, variableLocation, *location_list, command=set_location)
        optionsLocation.config(font=("Britannic bold", 15), bg="#f5faff", fg="#004080")
        optionsLocation.place(x=385, y=170, height=50, width=140)
    else:
        pass


def set_ref1(value):
    global ref1
    ref1 = value

def set_ref2(value):
    global ref2
    ref2 = value

def set_algorithm(value):
    global algorithm
    algorithm = value

def set_location(value):
    global location
    location = value


def predictScores():
    global hometeam
    global awayteam

    if ref1 == '' or ref2 == '' or location == '' or algorithm == '':
        messagebox.showwarning('Selecteer alle velden', 'Vul alle velden in om verder te gaan')
    else:
        home_teams = []
        away_teams = []
        for club in clubs:
            if club.get_clubnaam() in hometeam:
                home_teams = club.get_superteams()[hometeam]

            if club.get_clubnaam() in awayteam:
                away_teams = club.get_superteams()[awayteam]

        home_scores_df = get_team_score(home_teams, away_teams)
        away_scores_df = get_team_score(away_teams, home_teams)

        if algorithm == 'DecisionTree':
            home_predict = AlgorithmDecisionTree(home_scores_df, ref1, ref2, location).run()
            away_predict = AlgorithmDecisionTree(away_scores_df, ref1, ref2, location).run()
        elif algorithm == 'MultipleLR':
            home_predict = AlgorithmMLR(home_scores_df, ref1, ref2).run()
            away_predict = AlgorithmMLR(away_scores_df, ref1, ref2).run()
        elif algorithm == 'LinearRegression':
            home_predict = AlgorithmLinRegress(home_scores_df).run()
            away_predict = AlgorithmLinRegress(away_scores_df).run()

        result = '%.f - %.f' % (home_predict, away_predict)
        result2["text"] = '{}'.format(result)





# ------------------------------------------------------------------------------------------------------------------#
# Achtergrond #

C = Canvas(root, height=605, width=891)
filename = PhotoImage(file="../Floorballveld.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# ------------------------------------------------------------------------------------------------------------------#
# Frames #

frame1 = Frame(root, bg="#f5faff")
frame1.place(relx=0.15, rely=0.1, relwidth=0.6, relheight=0.5)

frame2 = Frame(root, bg="#f5faff")
frame2.place(relx=0.2, rely=0.65, relwidth=0.5, relheight=0.25)

frame3 = Frame(frame2, bg="#b4cce4")
frame3.place(relx=0.25, rely=0.55, relwidth=0.5, relheight=0.3)

# ------------------------------------------------------------------------------------------------------------------#
# Labels #

result1 = Label(master=frame2, text='Uitslag', height=1, bg="#f5faff", fg="#004080")
result1.config(font=("Britannic bold", 25))
result1.place(x=170, y=20)

result2 = Label(master=frame3, height=1, bg="#b4cce4", fg="#004080")
result2.config(font=("Britannic bold", 18))
result2.place(x=80, y=5)
# ------------------------------------------------------------------------------------------------------------------#
# buttons #

predictButton = Button(master=frame1, text='Voorspel', bg="#f5faff", fg="#004080", command=predictScores)
predictButton.config(font=("Britannic bold", 20))
predictButton.place(x=205, y=240)

NefubButton = Button(master=root, text='NeFUB site', bg="#b3cce6", fg="#004080")
NefubButton.config(font=("Calibri light", 10))
NefubButton.place(x=738, y=195)
NefubButton.bind("<Button-1>", lambda e: openWebsite("https://nefub.nl/floorball/"))

HUButton = Button(master=root, text='HU site', bg="#b3cce6", fg="#004080")
HUButton.config(font=("Calibri light", 10))
HUButton.place(x=747, y=383)
HUButton.bind("<Button-1>", lambda e: openWebsite("https://www.hu.nl/"))

# ------------------------------------------------------------------------------------------------------------------#
# optie menu's' #
clubs = create_club_objects(get_clubnames())
all_teams = create_superteams_list(clubs)
all_algorithms = ['DecisionTree', 'MultipleLR', 'LinearRegression']

variableHomeTeam = StringVar(frame1)
variableHomeTeam.set("Thuis team")
optionsHomeTeam = OptionMenu(frame1, variableHomeTeam, *all_teams, command=set_hometeam)
optionsHomeTeam.config(font=("Britannic bold", 25), bg="#f5faff", fg="#004080")
optionsHomeTeam.place(x=10, y=20, height=70, width=245)

variableAwayTeam = StringVar(frame1)
variableAwayTeam.set("Uit team")
optionsAwayTeam = OptionMenu(frame1, variableAwayTeam, *all_teams, command=set_awayteam)
optionsAwayTeam.config(font=("Britannic bold", 25), bg="#f5faff", fg="#004080")
optionsAwayTeam.place(x=280, y=20, height=70, width=245)

variableAlgorithm= StringVar(frame1)
variableAlgorithm.set("Algoritme")
optionsAlgorithm = OptionMenu(frame1, variableAlgorithm, *all_algorithms, command=set_algorithm)
optionsAlgorithm.config(font=("Britannic bold", 15), bg="#f5faff", fg="#004080")
optionsAlgorithm.place(x=10, y=170, height=50, width=140)
# ------------------------------------------------------------------------------------------------------------------#

root.mainloop()

# ------------------------------------------------------------------------------------------------------------------#
# Bronnen #

# https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
# https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter
# https://canvas.hu.nl/courses/12972/assignments/43477?module_item_id=162145
# https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter