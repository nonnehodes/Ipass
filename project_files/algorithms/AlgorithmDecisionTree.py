from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score

class AlgorithmDecisionTree:
    def __init__(self, team_scores_df, ref1=None, ref2=None, location=None):
        self.scores = team_scores_df.score
        self.target_team = team_scores_df.team[0]
        self.total_games = len(team_scores_df)
        self.df = team_scores_df
        self.ref1 = ref1
        self.ref2 = ref2
        self.location = location

    def run(self):
        '''
        Calculation for Decision Tree Regression

        Requires a DataFrame with the game statistics
        Target team for prediction vs. Opponent

        Algorithm will calculate prediction for Target team

        Additional features can be referee 1, referee 2, location

        :return: prediction value
        '''
        data = self.df
        features = ['index']
        if self.ref1:
            features.append('scheids1')
        if self.ref2:
            features.append('scheids2')
        if self.location:
            features.append('locatie')

        X = data[features].sort_values(by='index', ascending=True).reset_index(drop=True)
        string_cols = [col for col, dt in X.dtypes.items() if dt == object]
        df_dummies = pd.get_dummies(X[string_cols])
        X = X.drop(columns=string_cols).join(df_dummies)
        Y = data['score']


        model = DecisionTreeRegressor(random_state=0)
        model.fit(X, Y)

        # X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.8, test_size=0.2)
        # test = model.predict(X_test)
        # print(test)
        # eval = cross_val_score(model, X, Y, cv=5, scoring='neg_mean_squared_error')
        # print(eval)
        # print('\n')
        #
        # pd.DataFrame(X_test).to_csv('../notebook/prediction.csv')
        # plt.figure()
        # plt.scatter(X['index'], Y, s=20, edgecolor="black",
        #             c="darkorange", label="data")
        # plt.xlabel("index")
        # plt.ylabel("Score")
        # plt.title("Decision Tree Regression")
        # plt.legend()
        # plt.show()


        prediction = model.predict(self.create_prediction_array(X, features))
        # print('prediction = {}'.format(prediction))
        return prediction


    def create_prediction_array(self, X, features):
        new_row = {}
        for feature in features:
            if feature == 'index':
                new_row[feature] = self.total_games + 1
            elif feature == 'scheids1':
                for x in X.columns:
                    if self.ref1 in x:
                        col = x
                new_row[col] = 1
            elif feature == 'scheids2':
                for x in X.columns:
                    if self.ref2 in x:
                        col = x
                new_row[col] = 1
            elif feature == 'locatie':
                col = 'locatie_' + self.location
                new_row[col] = 1
        df = X.drop(X.index).append(new_row, ignore_index=True).fillna(0)
        return df




# AlgoritmeDecisionTree(pd.read_csv('output-utrecht.csv'), '7d44fdb4cd369049c23112395b915226', 'f8cd5ba4b8d3c0dade7c079fd87a3c3b', 'Amsterdam').run()