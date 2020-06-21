from project_files.Club import Club
from project_files.database.load_data import get_clubnames


def create_superteams_list(club_list):
    out = []
    for club in club_list:
        out += club.get_superteams()
    return out

def create_club_objects(clubs):
    out = []
    for name in get_clubnames():
        out.append(Club(name))
    return out