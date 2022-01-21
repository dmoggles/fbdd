import pandas as pd
from typing import Callable, Iterable, List, Union
import inspect
from fbdd.definitions import fbref_columns as fc
from fbdd.definitions import understat_columns as uc
from fbdd.definitions.core import DataAttribute, DataSources, DerivedDataAttribute, NativeDataAttribute
from functools import reduce
from fbdd.definitions.understat import TEAM_RENAMES
from fbdd.utils.fuzzy_merge import create_fuzzy_merge_reference_column

from fbdd.operations.filter import remove_non_top_5_teams


class Data:
    def __init__(self, data: pd.DataFrame):
        self._dataframe = data
        self._base_data = data
        self._data_unique_keys = [fc.PLAYER_ID, fc.DATE]

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, data: pd.DataFrame):
        self._dataframe = data

    @property
    def df(self):
        return self._dataframe

    @property
    def n(self):
        return len(self.dataframe)

    @property
    def base_data(self):
        return self._base_data

    @base_data.setter
    def base_data(self, data: pd.DataFrame):
        self._base_data = data

    @property
    def data_unique_keys(self):
        return self._data_unique_keys

    @data_unique_keys.setter
    def data_unique_keys(self, data_unique_keys: List[DataAttribute]):
        self._data_unique_keys = data_unique_keys

    def pipe(self, func: Callable, *args, **kwargs):
        func_spec = inspect.getfullargspec(func)
        if func_spec.args[0] == "base_data":

            calculation_result_df = self.dataframe.pipe(
                func, self.base_data, *args, **kwargs
            )
        else:
            calculation_result_df = self.dataframe.pipe(func, *args, **kwargs)

        data_to_return = Data(calculation_result_df)
        data_to_return.base_data = self.base_data
        if func.__name__ == "aggregate_by":
            if "aggregate_cols" in kwargs:
                data_to_return.data_unique_keys = kwargs["aggregate_cols"]
            else:
                data_to_return.data_unique_keys = args[0]
        else:
            data_to_return.data_unique_keys = self.data_unique_keys
        return data_to_return

    def merge(self, others: Iterable, how: str = "left", suffixes=("_x", "_y")):
        if not isinstance(others, Iterable):
            others = [others]

        data = reduce(
            lambda d1, d2: Data(
                pd.merge(
                    d1.dataframe,
                    d2.dataframe,
                    left_on=[k.N for k in d1.data_unique_keys],
                    right_on=[k.N for k in d2.data_unique_keys],
                    how=how,
                    suffixes=suffixes,
                )
            ),
            [self] + others,
        )
        data.base_data = self.base_data
        data.data_unique_keys = self.data_unique_keys
        return data

    def fuzzy_merge(self, other, fuzzy_this_col:DataAttribute, fuzzy_other_col:DataAttribute, this_cols:List[DataAttribute]=None, other_cols:List[DataAttribute]=None, how:str = "left", suffixes:tuple=("_x", "_y"), threshold:float = 0.8, limit:int=1):
        if not this_cols:
            this_cols = []
        if not other_cols:
            other_cols = []

        data = self.dataframe.copy()
        data = create_fuzzy_merge_reference_column(data, other.dataframe, fuzzy_this_col.N, fuzzy_other_col.N, threshold=threshold, limit=limit)
        merged_data = pd.merge(data, other.dataframe,left_on=[f'__fuzzy_{fuzzy_other_col.N}']+[c.N for c in this_cols], right_on=[fuzzy_other_col.N]+[c.N for c in other_cols], how=how, suffixes=suffixes)
        data_obj = Data(merged_data)
        data_obj.base_data = self.base_data
        data_obj.data_unique_keys = [fuzzy_this_col] + other_cols
        return data_obj

    def concat(self, others: Iterable):
        if not isinstance(others, Iterable):
            others = [others]
        data = Data(pd.concat([self.dataframe] + [o.dataframe for o in others]))
        data.base_data = self.base_data
        data.data_unique_keys = self.data_unique_keys
        return data

    def __getitem__(self, cols: Union[Iterable[DataAttribute], DataAttribute]):
        if not isinstance(cols, Iterable):
            cols = [cols]
        cols_to_get = self.data_unique_keys + cols
        new_data = Data(self.dataframe[[c.N for c in cols_to_get]])
        new_data.base_data = self.base_data
        new_data.data_unique_keys = self.data_unique_keys
        return new_data

    def cols(self, cols: Union[Iterable[DataAttribute], DataAttribute]):
        if not isinstance(cols, Iterable):
            cols = [cols]
        return self.dataframe[[c.N for c in cols]]

    def col(self, col: DataAttribute):
        return self.dataframe[col.N]


class FbRefData(Data):
    def __init__(self, years: List[int]):
        dfs = [
            pd.read_parquet(f"https://kovadata.herokuapp.com/data/f/{year}")
            for year in years
        ]
        data = pd.concat(dfs)
        data = remove_non_top_5_teams(data).drop_duplicates([fc.PLAYER_ID.N, fc.DATE.N])
        for c in DataAttribute._data_list:
            if isinstance(c, DerivedDataAttribute) and c.source==DataSources.FBREF:
                derived_col = c.apply(data)
                if isinstance(derived_col, pd.Series):
                    data[c.N] = derived_col

        super().__init__(data)

class UnderstatData(Data):
    def __init__(self, league:str, years:List[int]):
        dfs=[]
        for year in years:
            df = pd.read_parquet(f"https://kovadata.herokuapp.com/data/u/{league}/{year}") 
            if year < 2021:
                df=df.rename(columns={'year':'season'})
            dfs.append(df)
        
        data = pd.concat(dfs)
        for d in dir(uc):
            a = getattr(uc, d)
            
            if isinstance(a, NativeDataAttribute):
            
                data[a.N] = a.apply(data[a.N])
        #data[uc.HOME_TEAM.N] = data[uc.HOME_TEAM.N].replace(TEAM_RENAMES)
        #data[uc.AWAY_TEAM.N] = data[uc.AWAY_TEAM.N].replace(TEAM_RENAMES)
        data[uc.PLAYER_TEAM.N] = uc.PLAYER_TEAM.apply(data)
        super().__init__(data)
        self.data_unique_keys=[uc.ID]

            

