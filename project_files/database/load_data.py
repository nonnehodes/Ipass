import pandas as pd
import sqlite3

# https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python

def setup_connection():
    return sqlite3.connect("database/nefub.sqlite")

def load_data():
    file = 'datadump_nonne.csv'
    df = pd.read_csv(file)
    connection = setup_connection()
    df.to_sql('dames_competitie', connection, if_exists='append', index=False)


def get_club():
    con = setup_connection()
    cur = con.cursor()
    cur.execute("""SELECT DISTINCT thuisclub FROM dames_competitie""")
    rows = cur.fetchall()

    club_lijst = []
    for row in rows:
        club_lijst += row
    print(club_lijst)

def get_team_score(target_team, tegenstander):
    con = setup_connection()
    cur = con.cursor()
    cur.execute("""SELECT datum, thuisteam, thuisscore FROM dames_competitie WHERE thuisteam=? and uitteam=?""", (target_team, tegenstander))
    thuis_score = cur.fetchall()
    output = []
    for item in thuis_score:
        scores = {}
        scores['datum'] = item[0]
        scores['team'] = item[1]
        scores['uit_thuis'] = 'thuis'
        scores['score'] = item[2]
        output.append(scores)

    cur.execute("""SELECT datum, uitteam, uitscore FROM dames_competitie WHERE thuisteam=? and uitteam=?""", (tegenstander, target_team))
    uit_score = cur.fetchall()
    for item in uit_score:
        scores = {}
        scores['datum'] = item[0]
        scores['team'] = item[1]
        scores['uit_thuis'] = 'uit'
        scores['score'] = item[2]
        output.append(scores)

    df = pd.DataFrame(output)
    df['datum'] = pd.to_datetime(df.datum)
    df = df.sort_values(by='datum').reset_index()
    return df

print(get_team_score("UFC Utrecht 1", "Sonics"))
