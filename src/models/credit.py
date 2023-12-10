import pandas as pd


class Credit:
    columns = pd.read_csv("./data/credits_cleans.csv").columns

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
