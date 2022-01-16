
from typing import List
import pandas as pd

from fbdd.definitions.core import (
    DataAttribute,
    DerivedDataAttribute,
)
from fbdd.definitions import fbref_columns as fc

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
            try:
                db_agg[c.N] = c.apply(db_agg)
            except KeyError:
                pass
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

def common_minutes(data: pd.DataFrame) -> pd.DataFrame:
    def _common_minutes_agg(x):
        if len(x)>2:
            raise ValueError('Can only be used with 2 players')
        if len(x)< 2:
            return 0
        started=x[fc.STARTED.N].values
        minutes=x[fc.MINUTES.N].values
        if (started[0].startswith('Y') and started[1].startswith('Y')) or (started[0].startswith('Y') and started[1].startswith('Y')):
            return min(minutes)
        else:
            if started[0].startswith('Y'):
                return max( minutes[0]-(90-minutes[1]),0)
            else:
                return max(minutes[1]-(90-minutes[0]),0)

    common_minutes_data =  data.groupby([fc.COMPETITION.N, fc.TEAM.N, fc.OPPONENT.N, fc.DATE.N]).apply(_common_minutes_agg)
    common_minutes_data.name=fc.MINUTES.N
    return common_minutes_data.reset_index().sort_values(fc.DATE.N)
