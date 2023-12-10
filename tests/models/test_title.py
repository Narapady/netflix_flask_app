import pandas as pd

from src.models.title import Title


def test_title_instantiatation():
    values = pd.read_csv("./data/titles_cleans.csv")
    title = Title(values)
    assert type(title) == Title
