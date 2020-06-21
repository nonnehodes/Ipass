from project_files.database.load_data import setup_connection
import project_files.services.db_data

class Club:
    def __init__(self, clubnaam):
        self.clubnaam= clubnaam
        self.teams = self.get_team_names()

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


print(Club('UFC Utrecht').get_teams())
