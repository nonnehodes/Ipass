import pandas as pd
import sqlite3

# https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python

connection = sqlite3.connect("nefub.sqlite")

file = 'datadump_nonne.csv'
df = pd.read_csv(file)
df.to_sql('dames_competitie', connection, if_exists='append', index=False)