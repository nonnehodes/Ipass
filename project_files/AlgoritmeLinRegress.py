from scipy import polyval
from matplotlib.pyplot import plot, title, show, legend

class AlgoritmeLinRegress():
    def __init__(self, team_scores_df):
        self.scores = team_scores_df.score
        self.target_team = team_scores_df.team[0]
        self.aantal_wedstrijden = len(team_scores_df)
        self.df = team_scores_df

    def run(self):
        n = self.aantal_wedstrijden
        xn = self.scores
        data = self.df.score.reset_index().rename(columns={'index': 'y', 'score': 'x'})

        sumX = data.y.sum()
        sumX2 = data.y.apply(lambda x: x * x).sum()
        sumY = data.x.sum()
        sumXY = (data.x * data.y).sum()

        b = ((n * sumXY) - (sumX * sumY))/((n * sumX2) - (sumX * sumX))
        a = (sumY - b * sumX) / n

        # x = polyval([b, a], data.y)

        # title('Linear Regression Example')
        # plot(data.y, x, 'r--')
        # plot(data.y, xn, 'k.')
        # legend(['linregress', 'scores'])
        # show()

        return a + b*(n+1)

# https://scipy-cookbook.readthedocs.io/items/LinearRegression.html
