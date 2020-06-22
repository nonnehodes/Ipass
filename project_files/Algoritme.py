from scipy import linspace, polyval, polyfit, sqrt, stats, poly1d
from matplotlib.pyplot import plot, title, show, legend
from project_files.database.load_data import get_team_score

class Algoritme():
    def __init__(self, team_scores_df):
        self.scores = team_scores_df.score
        self.target_team = team_scores_df.team[0]
        self.aantal_wedstrijden = len(team_scores_df)

    def run(self):
        n = self.aantal_wedstrijden
        t = linspace(0, n, n)
        xn = self.scores

        model = polyfit(t, xn, 1)
        (ar, br) = model

        x = polyval(model, t)
        xr = polyval([ar, br], t)

        (a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)

        title('Linear Regression Example')
        plot(t, xn, 'k.')
        plot(t, xr, 'r.-')
        legend(['scores', 'linregress'])
        show()

        predict = poly1d(model)
        next_match = self.aantal_wedstrijden + 1
        return predict(next_match)

# https://scipy-cookbook.readthedocs.io/items/LinearRegression.html
