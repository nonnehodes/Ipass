class AlgorithmOwnDT:
    def __init__(self, team_score_df, ref1, ref2, location):
        self.total_games = len(team_score_df)
        self.scores =