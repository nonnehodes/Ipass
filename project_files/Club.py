from project_files.database.load_data import setup_connection

class Club:
    def __init__(self, clubnaam):
        self.clubnaam= clubnaam
        self.teams = self.get_team_names()

    def get_team_names(self):
        conn = setup_connection()
        cur = conn.cursor()
        cur.execute("""SELECT DISTINCT thuisteam FROM dames_competitie WHERE thuisclub = ?""", (self.clubnaam,))
        thuis = []
        for item in cur.fetchall():
            if not '2' in item[0]:
                thuis.append(item[0])
            else:
                continue

        cur.execute("""SELECT DISTINCT uitteam FROM dames_competitie WHERE uitclub = ?""", (self.clubnaam,))
        uit = []
        for item in cur.fetchall():
            if not '2' in item[0]:
                uit.append(item[0])
            else:
                continue

        return list(set(uit + thuis))

    def get_teams(self):
        return self.teams


print(Club('Sonics').get_teams())
