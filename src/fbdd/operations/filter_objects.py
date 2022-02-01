import abc
import pandas as pd
import numpy as np
from fbdd.definitions.core import DataAttribute


class FilterOperation(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def apply(frame: pd.DataFrame, column: pd.Series, value):
        pass


class GT(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, value):
        return frame.loc[column > value]


class GTE(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, value):
        return frame.loc[column >= value]


class LT(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, value):
        return frame.loc[column < value]


class LTE(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, value):
        return frame.loc[column <= value]


class EQ(FilterOperation):
    @staticmethod
    def apply(frame, column: pd.Series, value):
        return frame.loc[column == value]


class NEQ(FilterOperation):
    @staticmethod
    def apply(frame, column: pd.Series, value):
        return frame.loc[column != value]


class IsIn(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, values: list):
        return frame.loc[column.isin(values)]


class StrContainsOneOf(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, values: list):
        idx = np.array([False] * len(column))
        for v in values:
            idx = idx | (column.str.contains(v))
        return frame.loc[idx]


class Contains(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, value: str):
        return frame.loc[column.str.contains(value)]

class NotContains(FilterOperation):
    @staticmethod
    def apply(frame: pd.DataFrame, column: pd.Series, value: str):
        return frame.loc[~column.str.contains(value)]


class Filter:
    def __init__(self, column: DataAttribute, value, operation: FilterOperation):
        self._column = column
        self._value = value
        self._operation = operation

    def apply(self, df: pd.DataFrame):
        return self._operation.apply(df, df[self._column.N], self._value)
