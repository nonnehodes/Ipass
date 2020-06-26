from scipy import polyval
from matplotlib.pyplot import plot, title, show, legend
import numpy as np



class AlgorithmLinRegress():
    def __init__(self, team_scores_df):
        self.target_team = team_scores_df.team[0]
        self.total_games = len(team_scores_df)
        self.df = team_scores_df

    def run(self):
        '''
        Calculation for simple linear regression

        Requires a DataFrame with the game statistics
        Target team for prediction vs. Opponent

        Algorithm will calculate prediction for Target team

        :return: prediction value
        '''
        n = self.total_games
        data = self.df.score.reset_index()

        Y = data.score
        X = data.index

        x_mean = np.mean(X)
        y_mean = np.mean(Y)

        top = 0
        bottom = 0
        for i in range(n):
            top += (X[i] - x_mean) * (Y[i] - y_mean)
            bottom += (X[i] - x_mean) ** 2

        b = top / bottom
        a = y_mean - (b * x_mean)

        # print(a, b)
        # x = polyval([b, a], X)
        # xn = Y
        # title('Linear Regression Example')
        # plot(data.x, x, 'r--')
        # plot(data.x, xn, 'k.')
        # legend(['linregress', 'scores'])
        # show()
        # rmse = 0
        # for i in range(n):
        #     g = a + b * X[i]
        #     rmse += (Y[i] - g) ** 2
        #
        # rmse = np.sqrt(rmse / n)
        # print("LR rmse: {}".format(rmse))

        return a + b * (n + 1)

# https://scipy-cookbook.readthedocs.io/items/LinearRegression.html
