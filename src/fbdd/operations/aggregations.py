from typing import List
import pandas as pd

from fbdd.definitions.core import DataAttribute, DerivedDataAttribute, PctDerivedAttribute, RatioDerivedAttribute
from pandas.api.types import is_numeric_dtype
from fbdd.definitions import fbref_columns as fc


def aggregate_by(data: pd.DataFrame, aggregate_cols: List[DataAttribute]) -> pd.DataFrame:
    gb = data.groupby([c.N for c in aggregate_cols])
    transforms = {
        c: DataAttribute._name_data_map[c].agg_function
        for c in data.columns
        if DataAttribute._name_data_map[c].agg_function

    }
    db_agg = gb.agg(transforms)
    for c in DataAttribute._data_list:
        if isinstance(c, DerivedDataAttribute):
            db_agg[c.N] = c.apply(db_agg)
    indx_cols = db_agg.index.names

    db_agg = db_agg[set(db_agg.columns) - set(indx_cols)]
    return db_agg.reset_index()


def __per_90_rename(cols: List[str]) -> List[str]:
    return [f"{c}_per90" for c in cols]


def per_90(data: pd.DataFrame, rename: bool = False) -> pd.DataFrame:
    data_source = data.copy()
    columns_to_transform = [
        c
        for c in data_source.columns
        if is_numeric_dtype(data_source[c])
        and c not in [fc.MINUTES.name, fc.YEAR.name]
        and not (
            c in DataAttribute._name_data_map
            and isinstance(
                DataAttribute._name_data_map[c],
                (RatioDerivedAttribute, PctDerivedAttribute),
            )
        )
    ]
    for c in columns_to_transform:

        data_source[c] = data_source[c] / data_source[fc.MINUTES.name] * 90.0
    if rename:
        data_source = data_source.rename(
            columns={
                c: new_c
                for c, new_c in zip(columns_to_transform, __per_90_rename(columns_to_transform))
            }
        )
    return data_source


def __rank_rename(cols: List[str]) -> List[str]:
    return [f"{c}_rank" for c in cols]


def rank(data: pd.DataFrame, pct: bool = True, rename: bool = False) -> pd.DataFrame:
    ranked = data.rank(pct=pct, numeric_only=True)
    if rename:
        ranked = ranked.rename(
            columns={
                c: new_c for c, new_c in zip(ranked.columns, __rank_rename(ranked.columns))
            }
        )
    missing_cols = set(data.columns) - set(ranked.columns)

    for c in missing_cols:
        ranked[c] = data[c]
    return ranked
