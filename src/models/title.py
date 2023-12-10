import pandas as pd


class Title:
    columns = pd.read_csv("./data/titles_cleans.csv").columns

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
