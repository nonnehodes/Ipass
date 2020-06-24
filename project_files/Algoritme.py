from scipy import linspace, polyval, polyfit, sqrt, stats, poly1d
from matplotlib.pyplot import plot, title, show, legend
from project_files.database.load_data import get_team_score

class Algoritme():
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

        a = ((n * sumXY) - (sumX * sumY))/((n * sumX2) - (sumX * sumX))
        b = (sumY - a * sumX) / n
        print(a, b)

        x = polyval([a, b], data.y)

        title('Linear Regression Example')
        plot(data.y, x, 'g--')
        plot(data.y, xn, 'k.')
        legend(['linregress', 'scores'])
        show()

        predict = poly1d([a, b])
        next_match = self.aantal_wedstrijden + 1
        return predict(next_match)

# https://scipy-cookbook.readthedocs.io/items/LinearRegression.html
