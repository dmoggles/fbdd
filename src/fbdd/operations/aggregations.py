from typing import List
import pandas as pd

from fbdd.definitions.core import (
    DataAttribute,
    DerivedDataAttribute,
)


def aggregate_by(
    data: pd.DataFrame, aggregate_cols: List[DataAttribute]
) -> pd.DataFrame:
    gb = data.groupby([c.N for c in aggregate_cols])
    transforms = {
        c: DataAttribute._name_data_map[c].agg_function
        if c in DataAttribute._name_data_map
        and DataAttribute._name_data_map[c].agg_function
        else "sum"
        for c in data.columns
        if c not in DataAttribute._name_data_map
        or DataAttribute._name_data_map[c].agg_function
    }
    db_agg = gb.agg(transforms)
    for c in DataAttribute._data_list:
        if isinstance(c, DerivedDataAttribute):
            db_agg[c.N] = c.apply(db_agg)
    indx_cols = db_agg.index.names

    db_agg = db_agg[set(db_agg.columns) - set(indx_cols)]
    return db_agg.reset_index()


def __rank_rename(cols: List[str]) -> List[str]:
    return [f"{c}_rank" for c in cols]


def rank(data: pd.DataFrame, pct: bool = True, rename: bool = False) -> pd.DataFrame:
    ranked = data.rank(pct=pct, numeric_only=True)
    if rename:
        ranked = ranked.rename(
            columns={
                c: new_c
                for c, new_c in zip(ranked.columns, __rank_rename(ranked.columns))
            }
        )
    missing_cols = set(data.columns) - set(ranked.columns)

    for c in missing_cols:
        ranked[c] = data[c]
    return ranked
