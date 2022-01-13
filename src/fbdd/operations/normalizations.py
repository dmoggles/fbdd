from typing import List
import pandas as pd
from pandas.api.types import is_numeric_dtype
from fbdd.definitions import fbref_columns as fc
from fbdd.definitions.core import (
    DataAttribute,
    PctDerivedAttribute,
    RatioDerivedAttribute,
)


def __per_90_rename(cols: List[str], minutes: float) -> List[str]:
    return [f"{c}_per{int(minutes)}" for c in cols]


def per_90(data: pd.DataFrame, rename: bool = False) -> pd.DataFrame:
    data_source = extrapolate_to_minutes(data, 90)

    return data_source


def extrapolate_to_minutes(
    data: pd.DataFrame, minutes: float, rename: bool = False
) -> pd.DataFrame:
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

        data_source[c] = data_source[c] / data_source[fc.MINUTES.name] * minutes
    if rename:
        data_source = data_source.rename(
            columns={
                c: new_c
                for c, new_c in zip(
                    columns_to_transform, __per_90_rename(columns_to_transform, minutes)
                )
            }
        )
    return data_source


def normalize(data: pd.DataFrame) -> pd.DataFrame:
    data_source = data.copy()
    columns_to_transform = [
        c
        for c in data_source.columns
        if is_numeric_dtype(data_source[c]) and c not in [fc.MINUTES.name, fc.YEAR.name]
    ]
    for c in columns_to_transform:

        data_source[c] = (data_source[c] - data_source[c].mean()) / data_source[c].std()
    return data_source
