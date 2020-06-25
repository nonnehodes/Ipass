from scipy import polyval
from matplotlib.pyplot import plot, title, show, legend
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


class AlgoritmeMLR():
    def __init__(self, team_scores_df):
        self.target_team = team_scores_df.team[0]
        self.aantal_wedstrijden = len(team_scores_df)
        self.df = team_scores_df

    def run(self):
        n = self.aantal_wedstrijden
        data = self.df[['score', 'locatie']].reset_index()

        Y = data.score
        X = data.index
        X2 = data.locatie
        enc = LabelEncoder()
        X_enc = enc.fit_transform(y=X2)
        print(X_enc)

        x_enc_mean = np.mean(X_enc)
        print('Enc mean: {}'.format(x_enc_mean))
        x_mean = np.mean(X)
        y_mean = np.mean(Y)

        top = 0
        bottom = 0
        for i in range(n):
            top += (X[i] - x_mean) * (Y[i] - y_mean)
            bottom += (X[i] - x_mean) ** 2

        top2 = 0
        bottom2 = 0
        for i in range(n):
            top2 += (X[i] - x_mean) * (X_enc[i] - x_enc_mean)
            bottom2 += (X[i] - x_mean) ** 2

        b = top / bottom
        b2 = top2 / bottom2
        a = y_mean - (b * x_mean) - (b2 - x_enc_mean)

        print(a, b, b2)
        x = polyval([b, a], X)
        xr=[]
        for i in range(n):
            xr.append(a + b * (i + 1) + b2 * (i + 1))

        xn = data.score
        title('Linear Regression Example')
        plot(X, x, 'r--')
        plot(X, xn, 'k.')
        plot(X, xr, 'g.-')
        legend(['linregress', 'scores', 'MLR'])
        show()

        rmse = 0
        for i in range(n):
            g = a + b * X[i] + b2 * X[i]
            rmse += (Y[i] - g) ** 2

        rmse = np.sqrt(rmse / n)
        print("MLR rmse: {}".format(rmse))

        return a + b * (n + 1) + b2 * (n + 1)


# https://scipy-cookbook.readthedocs.io/items/LinearRegression.html
