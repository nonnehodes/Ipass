from unittest import TestCase
import pandas as pd

from project_files.algorithms.AlgorithmMLR import AlgorithmMLR


class TestAlgorithmMLR(TestCase):
    pass


class TestAlgorithmMLR(TestCase):
    def test_run(self):
        df = pd.read_csv('awayscores.csv')
        self.assertEqual(
            AlgorithmMLR(df, 'e89c6764cb79f40313364589a5651c40', 'a7c03e28b1abf335193b3b20f3282837').run(),
            6.56890331890332)
        df = pd.read_csv('homescores.csv')
        self.assertEqual(
            AlgorithmMLR(df, 'e89c6764cb79f40313364589a5651c40', 'a7c03e28b1abf335193b3b20f3282837').run(),
            1.5313131313131283)

    def test_create_prediction_array(self):
        df = pd.read_csv('awayscores.csv')
        features = ['index', 'ref1', 'ref2']
        X = df[features].sort_values(by='index', ascending=True).reset_index(drop=True)
        string_cols = [col for col, dt in X.dtypes.items() if dt == object]
        df_dummies = pd.get_dummies(X[string_cols])
        X = X.drop(columns=string_cols).join(df_dummies)
        out = AlgorithmMLR(df, 'e89c6764cb79f40313364589a5651c40', 'a7c03e28b1abf335193b3b20f3282837') \
            .create_prediction_array(X, features).to_dict()
        self.assertDictEqual(out, self.expected_dict())

    def expected_dict(self):
        return {'index': {0: 22.0}, 'ref1_041b0d41cac9e4bae468c10a0d0c3e18': {0: 0.0},
                'ref1_059fa46aafee60677cbde5d650c20872': {0: 0.0}, 'ref1_2e7e95078b58f771296abee439dca4cf': {0: 0.0},
                'ref1_47d4f1b75fb1cb6b3683ae567090ddad': {0: 0.0}, 'ref1_4df967cb47517e3e8d46b5b4ecddbe4d': {0: 0.0},
                'ref1_5f980d62fb20017607846e4250869d13': {0: 0.0}, 'ref1_6726dc565f3cebd78423a258d2d5a2cd': {0: 0.0},
                'ref1_782356bc86084494e137781fc42fc97a': {0: 0.0}, 'ref1_7d36a23fc64fac5394bbd1da73ecd2d9': {0: 0.0},
                'ref1_8bb5beca64ff936c6bd42eddfb89528b': {0: 0.0}, 'ref1_91ef982b8ec2c72272c9e32045feb336': {0: 0.0},
                'ref1_9f71d6e43d0c8799f38a92cb4a6231da': {0: 0.0}, 'ref1_b122057a3469d35d27c29a861f14c279': {0: 0.0},
                'ref1_d18d24182aa1598ea714358b12a49cb7': {0: 0.0}, 'ref1_dc0a68fd3435aa4160c74cc7037a8c1f': {0: 0.0},
                'ref1_de0357e8215d96f7a61d49ee5e3c1005': {0: 0.0}, 'ref1_e89c6764cb79f40313364589a5651c40': {0: 1.0},
                'ref1_f168b49418df8cdc224f3921a00f886d': {0: 0.0}, 'ref1_faf054dd8a2f0698429231110cc4b4b4': {0: 0.0},
                'ref2_203a6531f2ea38f37bef001d49d5228a': {0: 0.0}, 'ref2_2831a300ee95d4036990f0ad7990e849': {0: 0.0},
                'ref2_2f94911872153729c2d60dab06d98ae3': {0: 0.0}, 'ref2_3e646cb1ee1459bde439e4c337d3515c': {0: 0.0},
                'ref2_45f284466ef1e2542ee0aaf35a6e83b5': {0: 0.0}, 'ref2_47d4f1b75fb1cb6b3683ae567090ddad': {0: 0.0},
                'ref2_52c46476e8eb3f8ad03df1ebb9bb8727': {0: 0.0}, 'ref2_581d3c9fefbf642cbb169505d0e7dc60': {0: 0.0},
                'ref2_5fde3c3b8566edc6f7879f3336ba0b01': {0: 0.0}, 'ref2_6a646ddfdcae0e363688e155db05fa66': {0: 0.0},
                'ref2_8fb3699cef86f5f9c4c84df44eec32fe': {0: 0.0}, 'ref2_9aef3d1400d3cd17832f55af5c5af4ce': {0: 0.0},
                'ref2_a7c03e28b1abf335193b3b20f3282837': {0: 1.0}, 'ref2_be17171577738e0dfb43c18143024f42': {0: 0.0},
                'ref2_c13f8cf1de874f2373a47ce9e2b871b7': {0: 0.0}, 'ref2_c42386b84ff1ede5be28aa82d9b5d7dc': {0: 0.0},
                'ref2_d09092c686992605ccc2f6ad3fa74cad': {0: 0.0}, 'ref2_e0591c9945234368fbb8a972b55eb0c3': {0: 0.0},
                'ref2_ef164914477dd258f1a4da30cfa3529a': {0: 0.0}, 'ref2_f4a29fda5ec9060b7deeaa08a67af3b0': {0: 0.0},
                'ref2_ff6c0a290b7ebae41b211630d273b935': {0: 0.0}}
