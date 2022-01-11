import pandas as pd

from fbdd.operations.filter_objects import Filter
from typing import List
from fbdd.definitions import fbref_columns as fc

NON_TOP_5_TEAMS = ['CSKA Moscow', 'Spartak Moscow',
                   'Shakhtar', 'Loko Moscow', 'Krasnodar', 'Dynamo Mosc', 'Zenit',
                   'Rostov', 'Dynamo Kyiv', 'RB Salzburg', 'LASK', 'Rubin Kazan', 'Arsenal Tula', 'Samara', 'Sochi', 'Austria Wien', 'Sturm Graz', 'Rapid Wien', 'CS Emelec', 'Independiente']


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


def remove_non_top_5_teams(input_data: pd.DataFrame) -> pd.DataFrame:
    """ 
    Removes all rows with russian and austrian teams.  They are here because Russian premier league and English premier league have the same competition string in fbref, 
    as well as German Bundesliga and Austrian Bundesliga.

    Args:
        input_data (pd.DataFrame): Data to be filtered

    Returns:
        pd.DataFrame: Filtered data
    """
    return input_data[~input_data[fc.TEAM.N].isin(NON_TOP_5_TEAMS)]
