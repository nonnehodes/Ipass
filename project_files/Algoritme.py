from scipy import linspace, polyval, polyfit, sqrt, stats, poly1d
from matplotlib.pyplot import plot, title, show, legend
from project_files.database.load_data import get_team_score


class Algoritme():
    def __init__(self, team_scores_df):
        self.scores = team_scores_df.score
        self.target_team = team_scores_df.team[0]
        self.aantal_wedstrijden = len(team_scores_df)

    def run(self):
        # Algoritme van internet
        n = self.aantal_wedstrijden
        t = linspace(0, n, n)
        xn = self.scores
        poly = 4

        # Linear regressison -polyfit - polyfit can be used other orders polys
        model = polyfit(t, xn, 1)
        (ar, br) = model

        # Polynomial regression to th n-th order
        test = polyfit(t, xn, poly)
        x = polyval(test, t)

        xr = polyval([ar, br], t)
        # compute the mean square error
        err = sqrt(sum((xr - xn) ** 2) / n)
        print('Linear regression using polyfit')
        print('regression: a=%.2f b=%.2f, ms error= %.3f' % (ar, br, err))
        print('\n')

        # Linear regression using stats.linregress
        (a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
        print('Linear regression using stats.linregress')
        print('regression: a=%.2f b=%.2f, std error= %.3f' % (a_s, b_s, stderr))
        print('\n')

        # matplotlib ploting
        title('Linear Regression Example')
        plot(t, x,'g.--')
        plot(t, xn, 'k.')
        plot(t, xr, 'r.-')
        legend(['3-poly', 'scores', 'linregress'])
        show()

        predict = poly1d(test)
        next_match = self.aantal_wedstrijden + 1
        print(predict(next_match))
