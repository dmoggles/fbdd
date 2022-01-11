from typing import Literal
import pandas as pd


def add_literal(data: pd.DataFrame, col_name: str, literal: Literal) -> pd.DataFrame:
    data = data.copy()
    data[col_name] = literal
    return data
