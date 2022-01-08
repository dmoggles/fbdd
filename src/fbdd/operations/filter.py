import pandas as pd

from fbdd.operations.filter_objects import Filter
from typing import List
from fbdd.definitions import fbref_columns as fc

RUSSIAN_TEAMS = ['CSKA Moscow', 'Spartak Moscow',
                 'Shakhtar', 'Loko Moscow', 'Krasnodar', 'Dynamo Mosc', 'Zenit',
                 'Rostov', 'Dynamo Kyiv']


def apply_filter(input_data: pd.DataFrame, filters: List[Filter]) -> pd.DataFrame:
    """Applies selected filters to data

    Args:
        input_data (pd.DataFrame): Data to be filtered
        filters (List[Filter]): Filters to be applied

    Returns:
        pd.DataFrame: Filtered data
    """
    df = input_data.copy()
    for filter_ in filters:
        df = filter_.apply(df)
    return df


def remove_russian_teams(input_data: pd.DataFrame) -> pd.DataFrame:
    """ 
    Removes all rows with russian teams.  They are here because Russian premier league and English premier league have the same competition string in fbref

    Args:
        input_data (pd.DataFrame): Data to be filtered

    Returns:
        pd.DataFrame: Filtered data
    """
    return input_data[~input_data[fc.TEAM.N].isin(RUSSIAN_TEAMS)]
