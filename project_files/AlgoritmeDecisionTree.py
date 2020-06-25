from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class AlgoritmeDecisionTree:
    def __init__(self, team_scores_df):
        self.scores = team_scores_df.score
        self.target_team = team_scores_df.team[0]
        self.aantal_wedstrijden = len(team_scores_df)
        self.df = team_scores_df

    def run(self):
        n = self.aantal_wedstrijden
        data = self.df.reset_index()
        enc = LabelEncoder()
        data.locatie = enc.fit_transform(y=data.locatie)
        data.scheids1 = enc.fit_transform(y=data.scheids1)
        data.scheids2 = enc.fit_transform(y=data.scheids2)
        features =['index']
        X = data[features]
        Y = data['score']
        model = DecisionTreeRegressor(random_state=42)
        model.fit(X, Y)
        pred = [model.predict([[i]]) for i in range(n)]
        plt.figure()
        plt.scatter(X['index'], Y, s=20, edgecolor="black",
                    c="darkorange", label="data")
        plt.plot(X['index'], pred, color="yellowgreen", label="DCT", linewidth=1)
        plt.xlabel("index")
        plt.ylabel("Score")
        plt.title("Decision Tree Regression")
        plt.legend()
        plt.show()
        print(model.predict([[n+1]]))





AlgoritmeDecisionTree(pd.read_csv('output.csv')).run()