from project_files.database.load_data import setup_connection, get_club

class Club:
    def __init__(self, clubnaam):
        self.clubnaam = clubnaam
        self.teams = self.get_team_names()
        self.super_teams = self.groepeer_superteam()


    def __repr__(self):
        return str(self.clubnaam)

    def get_superteams(self):
        return self.super_teams

    def team_lijst(self, lijst):
        output = []
        for item in lijst:
            if not '29' in item[0]:
                output.append(item[0])
            else:
                continue
        return output

    def get_team_names_voor_2011(self):
        conn = setup_connection()
        cur = conn.cursor()
        out_voor_2011 = []

        cur.execute("""SELECT DISTINCT thuisteam FROM dames_competitie WHERE thuisclub = ? AND genre = ?  AND seizoen<2011 AND poule_naam LIKE "%1e Divisie%" """, (self.clubnaam, 'competitie'))
        out_voor_2011 += self.team_lijst(cur.fetchall())

        cur.execute("""SELECT DISTINCT uitteam FROM dames_competitie WHERE uitclub = ? AND genre = ? AND seizoen<2011 AND poule_naam LIKE "%1e Divisie%" """, (self.clubnaam, 'competitie'))
        out_voor_2011 += self.team_lijst(cur.fetchall())

        return list(set(out_voor_2011))

    def get_team_names_na_2011(self):
        conn = setup_connection()
        cur = conn.cursor()
        out_na_2001 = []

        cur.execute("""SELECT DISTINCT thuisteam FROM dames_competitie WHERE thuisclub = ? AND genre = ? AND seizoen>=2011 AND poule_naam LIKE "%Eredivisie%" """, (self.clubnaam, 'competitie'))
        out_na_2001 += self.team_lijst(cur.fetchall())

        cur.execute("""SELECT DISTINCT uitteam FROM dames_competitie WHERE uitclub = ? AND genre = ? AND seizoen>=2011 AND poule_naam LIKE "%Eredivisie%" """, (self.clubnaam, 'competitie'))
        out_na_2001 += self.team_lijst(cur.fetchall())

        return list(set(out_na_2001))

    def get_team_names(self):
        totaal_out = []
        totaal_out += self.get_team_names_voor_2011() + self.get_team_names_na_2011()

        return list(set(totaal_out))

    def get_teams(self):
        return self.teams

    def groepeer_superteam(self):
        out = {}
        teams = self.get_team_names()
        out[self.clubnaam + '-1'] = teams
        return out



def combi_data_club():
    lijst = get_club()
    out = []
    for naam in lijst:
        out.append(Club(naam))
    return out

print(combi_data_club())

temp = Club('Sonics').get_superteams()
print(temp)
