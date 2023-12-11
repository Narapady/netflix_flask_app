import pandas as pd
from flask import request


def build_query_args(model):
    keys = model.columns
    values = [request.args.get(col) for col in model.columns]
    query_args = dict(zip(keys, values))
    return {k: v for k, v in query_args.items() if v is not None}


def build_query_from_args(model):
    query_args = build_query_args(model)
    sql_str = "select * from title where "
    for k, v in query_args.items():
        sql_str += f"{k} = %s and "
    return sql_str[:-5] + ";"


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
