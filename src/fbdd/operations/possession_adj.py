import pandas as pd
from fbdd.definitions import fbref_columns as fc
from pandas.api.types import is_numeric_dtype
from fbdd.definitions.fbref import DATA_SETS, DEFENSE_DATA


def possession_factors(input_df: pd.DataFrame) -> pd.DataFrame:
    total_matches = len(input_df.groupby([fc.TEAM.N])) * (
        len(input_df.groupby([fc.TEAM.N])) - 1
    )
    total_matches_per_team = 2 * (len(input_df.groupby([fc.TEAM.N])) - 1)
    average_touches_per_match = input_df[fc.TOUCHES.N].sum() / total_matches
    team_touches = (
        input_df.groupby([fc.TEAM.N])
        .agg({fc.TOUCHES.N: "sum"})
        .rename(columns={fc.TOUCHES.N: "team_touches"})
    )
    opponent_touches = (
        input_df.groupby([fc.OPPONENT.N])
        .agg({fc.TOUCHES.N: "sum"})
        .rename(columns={fc.TOUCHES.N: "opponent_touches"})
    )
    df_all_touches = (
        pd.merge(team_touches, opponent_touches, left_index=True, right_index=True)
        / total_matches_per_team
    )
    df_all_touches["total_touches_per_game"] = (
        df_all_touches["team_touches"] + df_all_touches["opponent_touches"]
    )
    df_all_touches["pct_team_touches"] = (
        df_all_touches["team_touches"] / df_all_touches["total_touches_per_game"]
    )
    df_all_touches["pct_opponent_touches"] = (
        df_all_touches["opponent_touches"] / df_all_touches["total_touches_per_game"]
    )
    df_all_touches["total_touch_factor"] = (
        average_touches_per_match / df_all_touches["total_touches_per_game"]
    )
    df_all_touches["pct_in_possession_factor"] = (
        0.5 / df_all_touches["pct_team_touches"]
    )
    df_all_touches["pct_out_possession_factor"] = (
        0.5 / df_all_touches["pct_opponent_touches"]
    )
    df_all_touches["full_in_possession_mult"] = (
        df_all_touches["total_touch_factor"]
        * df_all_touches["pct_in_possession_factor"]
    )
    df_all_touches["full_out_possession_mult"] = (
        df_all_touches["total_touch_factor"]
        * df_all_touches["pct_out_possession_factor"]
    )
    return df_all_touches.reset_index().rename(columns={"index": fc.TEAM.N})


def possession_adjust(data: pd.DataFrame, full_data: pd.DataFrame) -> pd.DataFrame:
    pos_adj_factor_df = possession_factors(full_data)[
        ["squad", "pct_in_possession_factor", "pct_out_possession_factor"]
    ]
    df_combined = pd.merge(
        data, pos_adj_factor_df, left_on=fc.TEAM.N, right_on=fc.TEAM.N
    )
    columns_to_transform = [
        c
        for c in data.columns
        if is_numeric_dtype(data[c]) and c not in [fc.MINUTES.name, fc.YEAR.name]
    ]
    out_of_possession_sets = [c.name for c in DATA_SETS[DEFENSE_DATA]]
    for c in columns_to_transform:
        if c in out_of_possession_sets:
            df_combined[c] = df_combined[c] * df_combined["pct_out_possession_factor"]
        else:
            df_combined[c] = df_combined[c] * df_combined["pct_in_possession_factor"]

    missing_cols = set(data.columns) - set(df_combined.columns)
    for c in missing_cols:
        df_combined[c] = data[c]

    return df_combined
