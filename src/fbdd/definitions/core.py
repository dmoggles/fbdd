from typing import Callable, Union
import pandas as pd
import abc
import itertools


class DataAttribute:
    _name_data_map = {}
    _data_list = []

    def __init__(
        self,
        name: str,
        data_type: Union[str, type],
        agg_function: Callable,
        immutable: bool,
    ):
        self.name = name
        self.data_type = data_type
        self.agg_function = agg_function
        self.immutable = immutable
        self._data_list.append(self)

        self._name_data_map[self.name] = self

    @property
    def N(self):
        return self.name


class NativeDataAttribute(DataAttribute):
    def __init__(
        self,
        name,
        data_type,
        transform_function=None,
        rename_to=None,
        agg_function="sum",
        immutable=False,
    ):
        super().__init__(name, data_type, agg_function, immutable)
        self.transform_function = transform_function
        self.rename_to = rename_to

    def user_transform(self, column: pd.Series) -> pd.Series:
        if self.transform_function:
            return column.apply(self.transform_function)
        else:
            return column

    def pre_type_conversion_transform(self, column: pd.Series) -> pd.Series:
        return column

    def post_type_conversion_transform(self, column: pd.Series) -> pd.Series:
        return column

    def apply(self, column: pd.Series) -> pd.Series:
        column = self.user_transform(column)
        column = self.pre_type_conversion_transform(column)
        column = column.astype(self.data_type)
        column = self.post_type_conversion_transform(column)

        return column

    @property
    def N(self):
        if self.rename_to:
            return self.rename_to
        else:
            return self.name


class NumericDataAttribute(NativeDataAttribute):
    def __init__(
        self,
        name,
        data_type,
        transform_function=None,
        rename_to=None,
        agg_function="sum",
        immutable=False,
    ):
        super().__init__(
            name,
            data_type,
            transform_function=transform_function,
            rename_to=rename_to,
            agg_function=agg_function,
            immutable=immutable,
        )

    def pre_type_conversion_transform(self, column: pd.Series) -> pd.Series:
        return column.replace("", 0)

    def post_type_conversion_transform(self, column: pd.Series) -> pd.Series:
        return column.fillna(0)


class FloatDataAttribute(NumericDataAttribute):
    def __init__(
        self,
        name,
        transform_function=None,
        rename_to=None,
        agg_function="sum",
        immutable=False,
    ):
        super().__init__(
            name,
            "float",
            transform_function=transform_function,
            rename_to=rename_to,
            agg_function=agg_function,
            immutable=immutable,
        )


class IntDataAttribute(NumericDataAttribute):
    def __init__(
        self,
        name,
        transform_function=None,
        rename_to=None,
        agg_function="sum",
        immutable=False,
    ):
        super().__init__(
            name,
            "int",
            transform_function=transform_function,
            rename_to=rename_to,
            agg_function=agg_function,
            immutable=immutable,
        )


class StrDataAttribute(NativeDataAttribute):
    def __init__(
        self, name, transform_function=None, rename_to=None, agg_function="first"
    ):
        super().__init__(
            name,
            "str",
            transform_function=transform_function,
            rename_to=rename_to,
            agg_function=agg_function,
            immutable=False,
        )


class DateDataAttribute(NativeDataAttribute):
    def __init__(
        self, name, transform_function=None, rename_to=None, agg_function="first"
    ):
        super().__init__(
            name,
            "datetime64",
            transform_function=transform_function,
            rename_to=rename_to,
            agg_function=agg_function,
            immutable=False,
        )


class DerivedDataAttribute(DataAttribute, abc.ABC):
    def __init__(self, name: str, data_type: Union[str, type], agg_function: Callable):
        super().__init__(name, data_type, agg_function, immutable=False)

    @abc.abstractmethod
    def apply(self, data: pd.DataFrame) -> pd.Series:
        pass


class PctDerivedAttribute(DerivedDataAttribute):
    def __init__(
        self,
        name: str,
        numerator_data: DataAttribute,
        denominator_data: DataAttribute,
    ):
        super().__init__(name, "float", None)
        self.numerator_data = numerator_data
        self.denominator_data = denominator_data

    def apply(self, data: pd.DataFrame) -> pd.Series:
        if (
            self.numerator_data.N in data.columns
            and self.denominator_data.N in data.columns
        ):
            return (
                data[self.numerator_data.N] /
                data[self.denominator_data.N] * 100
            ).fillna(0)


class RatioDerivedAttribute(DerivedDataAttribute):
    def __init__(
        self,
        name: str,
        numerator_data: DataAttribute,
        denominator_data: DataAttribute,
    ):
        super().__init__(name, "float", None)
        self.numerator_data = numerator_data
        self.denominator_data = denominator_data

    def apply(self, data: pd.DataFrame) -> pd.Series:
        if (
            self.numerator_data.N in data.columns
            and self.denominator_data.N in data.columns
        ):
            return (
                data[self.numerator_data.N] / data[self.denominator_data.N]
            ).fillna(0)


class DiffDerivedAttribute(DerivedDataAttribute):
    def __init__(
        self,
        name: str,
        baseline: DataAttribute,
        subtractor: DataAttribute,
    ):
        super().__init__(name, "float", None)
        self.baseline = baseline
        self.subtractor = subtractor

    def apply(self, data: pd.DataFrame) -> pd.Series:
        if self.baseline.N in data.columns and self.subtractor.N in data.columns:
            return (data[self.baseline.N] -
                    data[self.subtractor.N]).fillna(0)


class SumDerivedAttribute(DerivedDataAttribute):
    def __init__(
        self,
        name: str,
        stat1: DataAttribute,
        stat2: DataAttribute,
    ):
        super().__init__(name, "float", None)
        self.stat1 = stat1
        self.stat2 = stat2

    def apply(self, data: pd.DataFrame) -> pd.Series:
        if self.stat1.N in data.columns and self.stat2.N in data.columns:
            return (data[self.stat1.N] + data[self.stat2.N]).fillna(0)


def list_all_values(s: pd.Series) -> pd.Series:
    return ",".join(set(itertools.chain(*[x.split(",") for x in s.unique()])))
