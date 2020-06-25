import pandas as pd
import sqlite3



def setup_connection():
    return sqlite3.connect("database/nefub.sqlite")

def load_data():
    file = 'datadump_nonne.csv'
    df = pd.read_csv(file)
    connection = setup_connection()
    df.to_sql('dames_competitie', connection, if_exists='append', index=False)


def get_clubnames():
    con = setup_connection()
    cur = con.cursor()
    cur.execute("""SELECT DISTINCT thuisclub FROM dames_competitie""")
    rows = cur.fetchall()
    club_list = []
    for row in rows:
        club_list += row
    return club_list

def get_team_history(teams):
    con = setup_connection()
    df = pd.DataFrame()
    for team in teams:
        tp =  pd.read_sql_query('SELECT * FROM dames_competitie WHERE thuisteam=? OR uitteam=? AND genre=?', con, params=(team, team, 'competitie'))
        df = df.append(tp)
    df.to_csv('teams.csv', index=False)
    return df


def get_team_score(target_teams, tegenstanders):
    con = setup_connection()
    cur = con.cursor()
    output = []
    for target_team in target_teams:
        for tegenstander in tegenstanders:
            cur.execute("""SELECT datum, thuisteam, thuisscore, scheids1_hashed, scheids2_hashed, plaats_sporthal FROM dames_competitie WHERE thuisteam=? and uitteam=?""", (target_team, tegenstander))
            thuis_score = cur.fetchall()

            for item in thuis_score:
                scores = {}
                scores['datum'] = item[0]
                scores['team'] = item[1]
                scores['uit_thuis'] = 'thuis'
                scores['score'] = item[2]
                scores['scheids1'] = item[3]
                scores['scheids2'] = item[4]
                scores['locatie'] = item[5]
                output.append(scores)

            cur.execute("""SELECT datum, uitteam, uitscore, scheids1_hashed, scheids2_hashed, plaats_sporthal FROM dames_competitie WHERE thuisteam=? and uitteam=?""", (tegenstander, target_team))
            uit_score = cur.fetchall()
            for item in uit_score:
                scores = {}
                scores['datum'] = item[0]
                scores['team'] = item[1]
                scores['uit_thuis'] = 'uit'
                scores['score'] = item[2]
                scores['scheids1'] = item[3]
                scores['scheids2'] = item[4]
                scores['locatie'] = item[5]
                output.append(scores)

    df = pd.DataFrame(output)
    df['datum'] = pd.to_datetime(df.datum)
    df = df.sort_values(by='datum').reset_index()
    df.to_csv('output.csv', index=False)
    return df

def get_team_names_voor_2011(clubnaam):
    conn = setup_connection()
    cur = conn.cursor()
    out_voor_2011 = []

    cur.execute("""SELECT DISTINCT thuisteam FROM dames_competitie WHERE thuisclub = ? AND genre = ?  AND seizoen<2011 AND poule_naam LIKE "%1e Divisie%" """, (clubnaam, 'competitie'))
    out_voor_2011 += clean_query_results(cur.fetchall())

    cur.execute("""SELECT DISTINCT uitteam FROM dames_competitie WHERE uitclub = ? AND genre = ? AND seizoen<2011 AND poule_naam LIKE "%1e Divisie%" """, (clubnaam, 'competitie'))
    out_voor_2011 += clean_query_results(cur.fetchall())
    return list(set(out_voor_2011))

def get_team_names_na_2011(clubnaam):
    conn = setup_connection()
    cur = conn.cursor()
    out_na_2001 = []

    cur.execute("""SELECT DISTINCT thuisteam FROM dames_competitie WHERE thuisclub = ? AND genre = ? AND seizoen>=2011 AND poule_naam LIKE "%Eredivisie%" """, (clubnaam, 'competitie'))
    out_na_2001 += clean_query_results(cur.fetchall())

    cur.execute("""SELECT DISTINCT uitteam FROM dames_competitie WHERE uitclub = ? AND genre = ? AND seizoen>=2011 AND poule_naam LIKE "%Eredivisie%" """, (clubnaam, 'competitie'))
    out_na_2001 += clean_query_results(cur.fetchall())
    return list(set(out_na_2001))

def get_scheidsrechters():
    conn = sqlite3.connect("nefub.sqlite")
    cur = conn.cursor()
    scheidsrechters_lijst_hashed = []

    cur.execute("""SELECT DISTINCT scheids1_hashed FROM dames_competitie""")
    scheidsrechters_lijst_hashed += clean_query_results(cur.fetchall())

    cur.execute("""SELECT DISTINCT scheids2_hashed FROM dames_competitie""")
    scheidsrechters_lijst_hashed += clean_query_results(cur.fetchall())

    print(list(set(scheidsrechters_lijst_hashed)))
    return list(set(scheidsrechters_lijst_hashed))

def clean_query_results(results):
    out = []
    for row in results:
        out.append(row[0])
    return out


# https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
