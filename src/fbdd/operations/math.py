from typing import Union
import pandas as pd


def add_literal(data: pd.DataFrame, col_name: str, literal: Union[str, int, float]) -> pd.DataFrame:
    data = data.copy()
    data[col_name] = literal
    return data
