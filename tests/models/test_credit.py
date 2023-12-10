import pandas as pd

from src.models.credit import Credit


def test_credit_instantiatation():
    values = pd.read_csv("./data/credits_cleans.csv")
    credit = Credit(values)
    assert type(credit) == Credit
