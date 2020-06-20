import sqlite3

def setup_connection():
    return sqlite3.connect("../../database/nefub.sqlite")

def get_club():
    con = setup_connection()
    cur = con.cursor()
    cur.execute("""SELECT DISTINCT thuisclub FROM dames_competitie""")
    rows = cur.fetchall()

    club_lijst = []
    for row in rows:
        club_lijst += row
    print(club_lijst)

