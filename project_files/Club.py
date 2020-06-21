from collections import defaultdict
from project_files.database.load_data import get_team_names_na_2011, get_team_names_voor_2011

class Club:
    def __init__(self, clubnaam):
        self.clubnaam = clubnaam
        self.teams = self.get_team_names()
        self.super_teams = self.groepeer_superteam()


    def __repr__(self):
        return str(self.clubnaam)

    def get_superteams(self):
        return self.super_teams

    def get_team_names(self):
        totaal_out = []
        totaal_out += get_team_names_voor_2011(self.clubnaam) + get_team_names_na_2011(self.clubnaam)
        return list(set(totaal_out))

    def get_teams(self):
        return self.teams

    def groepeer_superteam(self):
        out = defaultdict(list)
        team_names = self.get_team_names()
        for team_name in team_names:
            if "2" in team_name:
                out[self.clubnaam + '-2'].append(team_name)
            else:
                out[self.clubnaam + '-1'].append(team_name)
        return out
