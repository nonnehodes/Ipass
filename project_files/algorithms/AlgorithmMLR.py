from scipy import polyval
from matplotlib.pyplot import plot, title, show, legend
import numpy as np
import pandas as pd


class AlgorithmMLR():
    def __init__(self, team_scores_df, scheids1=None, scheids2=None):
        self.target_team = team_scores_df.team[0]
        self.aantal_wedstrijden = len(team_scores_df)
        self.df = team_scores_df
        self.scheids1 = scheids1
        self.scheids2 = scheids2

    def run(self):
        n = self.aantal_wedstrijden
        data = self.df
        x_axis = data.index

        features = ['index']
        if self.scheids1:
            features.append('scheids1')
        if self.scheids2:
            features.append('scheids2')

        X = data[features].sort_values(by='index', ascending=True).reset_index(drop=True)
        string_cols = [col for col, dt in X.dtypes.items() if dt == object]
        df_dummies = pd.get_dummies(X[string_cols])
        X = X.drop(columns=string_cols).join(df_dummies)
        y = data.score
        y_mean = data.score.mean()
        all_coeffs = {}  # {no_term: [b, for_a]
        for j, col in enumerate(X.columns):
            x_mean = X[col].mean()
            top = 0
            bottom = 0
            for i in range(n):
                top += (X[col][i] - x_mean) * (y[i] - y_mean)
                bottom += (X[col][i] - x_mean) ** 2
            b = top / bottom
            all_coeffs[j] = [b, b * x_mean]
        # print('all coeffs: {}'.format(all_coeffs))

        total = 0
        for item in all_coeffs.values():
            total += item[1]
        a = y_mean - total
        print('a: {}'.format(a))

        y_temp = []
        for i in range(n):
            for j, col in enumerate(X.columns):
                temp = []
                temp.append(all_coeffs[j][0] * X[col][i])  # b1 * X[1]n -> b2 * X[2]n
            y_temp.append(sum(temp))
        y_mlr = [a + x for x in y_temp]

        # title('Linear Regression Example')
        # plot(x_axis, y, 'k.')
        # plot(x_axis, y_mlr, 'r--')
        # legend(['Scores', 'MLR'])
        # show()
        #
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
        print('prediction = {}'.format(prediction))
        return prediction

    def create_prediction_array(self, X, features):
        new_row = {}
        for feature in features:
            if feature == 'index':
                new_row[feature] = self.aantal_wedstrijden + 1
            elif feature == 'scheids1':
                for x in X.columns:
                    if self.scheids1 in x:
                        col = x
                new_row[col] = 1
            elif feature == 'scheids2':
                for x in X.columns:
                    if self.scheids2 in x:
                        col = x
                new_row[col] = 1
        df = X.drop(X.index).append(new_row, ignore_index=True).fillna(0)
        df.to_csv('mlr.csv')
        return df

# AlgoritmeMLR(pd.read_csv('output-utrecht.csv'), '7d44fdb4cd369049c23112395b915226', 'f8cd5ba4b8d3c0dade7c079fd87a3c3b').run()
# https://scipy-cookbook.readthedocs.io/items/LinearRegression.html
