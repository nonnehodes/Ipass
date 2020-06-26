from scipy import polyval
from matplotlib.pyplot import plot, title, show, legend
import numpy as np
import pandas as pd


class AlgorithmMLR():
    def __init__(self, team_scores_df, ref1=None, ref2=None):
        self.total_games = len(team_scores_df)
        self.df = team_scores_df
        self.ref1 = ref1
        self.ref2 = ref2

    def run(self):
        '''
        Calculation for multiple linear regression

        Requires a DataFrame with the game statistics
        Target team for prediction vs. Opponent

        Algorithm will calculate prediction for Target team

        Additional features can be referee 1 and referee 2

        :return: prediction value
        '''

        n = self.total_games
        data = self.df

        features = ['index']
        if self.ref1:
            features.append('ref1')
        if self.ref2:
            features.append('ref2')

        X = data[features].sort_values(by='index', ascending=True).reset_index(drop=True)
        string_cols = [col for col, dt in X.dtypes.items() if dt == object]
        df_dummies = pd.get_dummies(X[string_cols])
        X = X.drop(columns=string_cols).join(df_dummies)
        y = data.score
        y_mean = data.score.mean()
        all_coeffs = {}
        for j, col in enumerate(X.columns):
            x_mean = X[col].mean()
            top = 0
            bottom = 0
            for i in range(n):
                top += (X[col][i] - x_mean) * (y[i] - y_mean)
                bottom += (X[col][i] - x_mean) ** 2
            b = top / bottom
            all_coeffs[j] = [b, b * x_mean]

        total = 0
        for item in all_coeffs.values():
            total += item[1]
        a = y_mean - total
        # print('a: {}'.format(a))

        y_temp = []
        for i in range(n):
            for j, col in enumerate(X.columns):
                temp = []
                temp.append(all_coeffs[j][0] * X[col][i])
            y_temp.append(sum(temp))

        # y_mlr = [a + x for x in y_temp]
        # title('Linear Regression Example')
        # plot(x_axis, y, 'k.')
        # plot(x_axis, y_mlr, 'r--')
        # legend(['Scores', 'MLR'])
        # show()
        # rmse = 0
        # for i in range(n):
        #     rmse += (y[i] - y_mlr[i]) ** 2
        #
        # rmse = np.sqrt(rmse / n)
        # print("MLR rmse: {}".format(rmse))

        p = self.create_prediction_array(X, features)
        for j, col in enumerate(p.columns):
            temp = []
            temp.append(all_coeffs[j][0] * p[col][0])
        prediction = a + sum(temp)
        # print('prediction = {}'.format(prediction))
        return prediction

    def create_prediction_array(self, X, features):
        new_row = {}
        for feature in features:
            if feature == 'index':
                new_row[feature] = self.total_games + 1
            elif feature == 'ref1':
                for x in X.columns:
                    if self.ref1 in x:
                        col = x
                new_row[col] = 1
            elif feature == 'ref2':
                for x in X.columns:
                    if self.ref2 in x:
                        col = x
                new_row[col] = 1
        df = X.drop(X.index).append(new_row, ignore_index=True).fillna(0)
        return df

# https://scipy-cookbook.readthedocs.io/items/LinearRegression.html
