from typing import Union
import pandas as pd

from fbdd.definitions.core import DataAttribute


def add_literal(
    data: pd.DataFrame, col_name: DataAttribute, literal: Union[str, int, float]
) -> pd.DataFrame:
    data = data.copy()
    data[col_name.N] = literal
    return data
