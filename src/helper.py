import pandas as pd


def bulid_insert_query(model):
    cols = pd.read_csv(f"./data/{model}s_cleans.csv").columns
    insert_into = f"INSERT INTO {model} ({[col for col in cols]})\
                            VALUES ({['%s' for _ in range(len(cols))]} )"
    insert_into = (
        insert_into.replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace("    ", "")
    )

    return insert_into


def build_insert_data(model):
    df = pd.read_csv(f"./data/{model}s_cleans.csv").iloc[:5, :]
    data_dicts = df.to_dict("records")
    return [tuple([v for k, v in data_dict.items()]) for data_dict in data_dicts]