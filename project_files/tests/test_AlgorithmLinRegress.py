from unittest import TestCase
import pandas as pd

from project_files.algorithms.AlgorithmLinRegress import AlgorithmLinRegress


class TestAlgorithmLinRegress(TestCase):
    def test_run(self):
        df = pd.read_csv('awayscores.csv')
        self.assertEqual(AlgorithmLinRegress(df).run(), 1.6839826839826841)
        df2 = pd.read_csv('homescores.csv')
        self.assertEqual(AlgorithmLinRegress(df2).run(), 11.785281385281385)
