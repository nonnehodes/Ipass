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
