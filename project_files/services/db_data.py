import sqlite3

def setup_connection():
    return sqlite3.connect("../../database/nefub.sqlite")

def get_team():
    con = setup_connection()
    cur = con.cursor()
    cur.execute("""SELECT DISTINCT thuisclub FROM dames_competitie""")
    rows = cur.fetchall()

    team_lijst = []
    for row in rows:
        team_lijst += row
    print(team_lijst)

get_team()