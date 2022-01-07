from fbdd.definitions.core import (
    DateDataAttribute,
    FloatDataAttribute,
    IntDataAttribute,
    StrDataAttribute,
)
import pandas as pd
import itertools

VALID_LEAGUES = [
    "Ligue 1",
    "Premier League",
    "Champions Lg",
    "La Liga",
    "Serie A",
    "Bundesliga",
]
SUMMARY_DATA = "summary"
PASSING_DATA = "passing"
PASSING_TYPES_DATA = "passing_types"
GCA_DATA = "gca"
DEFENSE_DATA = "defense"
POSSESSION_DATA = "possession"
MISC_DATA = "misc"
KEEPER_DATA = "keepersadv"

DATA_TYPES = [
    SUMMARY_DATA,
    PASSING_DATA,
    PASSING_TYPES_DATA,
    GCA_DATA,
    DEFENSE_DATA,
    POSSESSION_DATA,
    MISC_DATA,
]
KEEPER_TYPES = [KEEPER_DATA]


def list_all_values(s: pd.Series) -> pd.Series:
    return ",".join(set(itertools.chain(*[x.split(",") for x in s.unique()])))


YEAR = IntDataAttribute("season", agg_function="first", immutable=True)
PLAYER_ID = StrDataAttribute("player_id")
PLAYER = StrDataAttribute("player")
DATE = DateDataAttribute("date", agg_function=None)
DAY_OF_WEEK = StrDataAttribute("dayofweek", agg_function=None)
COMPETITION = StrDataAttribute("comp", agg_function=list_all_values)
ROUND = StrDataAttribute("round", agg_function=None)
VENUE = StrDataAttribute("venue", agg_function=None)
RESULT = StrDataAttribute("result", agg_function=None)
TEAM = StrDataAttribute("squad", agg_function=list_all_values)
OPPONENT = StrDataAttribute("opponent", agg_function=None)
STARTED = StrDataAttribute("game_started", agg_function=None)
POSITION = StrDataAttribute("position", agg_function=list_all_values)
MINUTES = FloatDataAttribute("minutes", immutable=True)
TACKLES = FloatDataAttribute("tackles")
TACKLES_WON = FloatDataAttribute("tackles_won")
TACKLES_DEF_3RD = FloatDataAttribute("tackles_def_3rd")
TACKLES_MID_3RD = FloatDataAttribute("tackles_mid_3rd")
TACKLES_ATT_3RD = FloatDataAttribute("tackles_att_3rd")
DRIBBLE_TACKLES = FloatDataAttribute("dribble_tackles")
DRIBBLES_VS = FloatDataAttribute("dribbles_vs")
DRIBBLED_PAST = FloatDataAttribute("dribbled_past")
PRESSURES = FloatDataAttribute("pressures")
PRESSURE_REGAINS = FloatDataAttribute("pressure_regains")
PRESSURES_DEF_3RD = FloatDataAttribute("pressures_def_3rd")
PRESSURES_MID_3RD = FloatDataAttribute("pressures_mid_3rd")
PRESSURES_ATT_3RD = FloatDataAttribute("pressures_att_3rd")
BLOCKS = FloatDataAttribute("blocks")
BLOCKED_SHOTS = FloatDataAttribute("blocked_shots")
BLOCKED_SHOTS_SAVES = FloatDataAttribute("blocked_shots_saves")
BLOCKED_PASSES = FloatDataAttribute("blocked_passes")
INTERCEPTIONS = FloatDataAttribute("interceptions")
TACKLES_INTERCEPTIONS = FloatDataAttribute("tackles_interceptions")
CLEARANCES = FloatDataAttribute("clearances")
ERRORS = FloatDataAttribute("errors")
BENCH_EXPLAIN = StrDataAttribute("bench_explain", agg_function=None)

SCA = FloatDataAttribute("sca")
SCA_PASSES_LIVE = FloatDataAttribute("sca_passes_live")
SCA_PASSES_DEAD = FloatDataAttribute("sca_passes_dead")
SCA_DRIBBLES = FloatDataAttribute("sca_dribbles")
SCA_SHOTS = FloatDataAttribute("sca_shots")
SCA_FOULED = FloatDataAttribute("sca_fouled")
SCA_DEFENSE = FloatDataAttribute("sca_defense")
GCA = FloatDataAttribute("gca")
GCA_PASSES_LIVE = FloatDataAttribute("gca_passes_live")
GCA_PASSES_DEAD = FloatDataAttribute("gca_passes_dead")
GCA_DRIBBLES = FloatDataAttribute("gca_dribbles")
GCA_SHOTS = FloatDataAttribute("gca_shots")
GCA_FOULED = FloatDataAttribute("gca_fouled")
GCA_DEFENSE = FloatDataAttribute("gca_defense")


PASSES_COMPLETED = FloatDataAttribute("passes_completed")
PASSES = FloatDataAttribute("passes")

PASSES_TOTAL_DISTANCE = FloatDataAttribute("passes_total_distance")
PASSES_PROGRESSIVE_DISTANCE = FloatDataAttribute("passes_progressive_distance")
PASSES_COMPLETED_SHORT = FloatDataAttribute("passes_completed_short")
PASSES_SHORT = FloatDataAttribute("passes_short")

PASSES_COMPLETED_MEDIUM = FloatDataAttribute("passes_completed_medium")
PASSES_MEDIUM = FloatDataAttribute("passes_medium")

PASSES_COMPLETED_LONG = FloatDataAttribute("passes_completed_long")
PASSES_LONG = FloatDataAttribute("passes_long")

ASSISTS = FloatDataAttribute("assists")
XA = FloatDataAttribute("xa")
ASSISTED_SHOTS = FloatDataAttribute("assisted_shots")
PASSES_INTO_FINAL_THIRD = FloatDataAttribute("passes_into_final_third")
PASSES_INTO_PENALTY_AREA = FloatDataAttribute("passes_into_penalty_area")
CROSSES_INTO_PENALTY_AREA = FloatDataAttribute("crosses_into_penalty_area")
PROGRESSIVE_PASSES = FloatDataAttribute("progressive_passes")

PASSES_LIVE = FloatDataAttribute("passes_live")
PASSES_DEAD = FloatDataAttribute("passes_dead")
PASSES_FREE_KICKS = FloatDataAttribute("passes_free_kicks")
THROUGH_BALLS = FloatDataAttribute("through_balls")
PASSES_PRESSURE = FloatDataAttribute("passes_pressure")
PASSES_SWITCHES = FloatDataAttribute("passes_switches")
CROSSES = FloatDataAttribute("crosses")
CORNER_KICKS = FloatDataAttribute("corner_kicks")
CORNER_KICKS_IN = FloatDataAttribute("corner_kicks_in")
CORNER_KICKS_OUT = FloatDataAttribute("corner_kicks_out")
CORNER_KICKS_STRAIGHT = FloatDataAttribute("corner_kicks_straight")
PASSES_GROUND = FloatDataAttribute("passes_ground")
PASSES_LOW = FloatDataAttribute("passes_low")
PASSES_HIGH = FloatDataAttribute("passes_high")
PASSES_LEFT_FOOT = FloatDataAttribute("passes_left_foot")
PASSES_RIGHT_FOOT = FloatDataAttribute("passes_right_foot")
PASSES_HEAD = FloatDataAttribute("passes_head")
THROW_INS = FloatDataAttribute("throw_ins")
PASSES_OTHER_BODY = FloatDataAttribute("passes_other_body")
PASSES_COMPLETED = FloatDataAttribute("passes_completed")
PASSES_OFFSIDES = FloatDataAttribute("passes_offsides")
PASSES_OOB = FloatDataAttribute("passes_oob")
PASSES_INTERCEPTED = FloatDataAttribute("passes_intercepted")
PASSES_BLOCKED = FloatDataAttribute("passes_blocked")

CARDS_YELLOW = FloatDataAttribute("cards_yellow")
CARDS_RED = FloatDataAttribute("cards_red")
CARDS_YELLOW_RED = FloatDataAttribute("cards_yellow_red")
FOULS = FloatDataAttribute("fouls")
FOULED = FloatDataAttribute("fouled")
OFFSIDES = FloatDataAttribute("offsides")
CROSSES = FloatDataAttribute("crosses")
INTERCEPTIONS = FloatDataAttribute("interceptions")
TACKLES_WON = FloatDataAttribute("tackles_won")
PENS_WON = FloatDataAttribute("pens_won")
PENS_CONCEDED = FloatDataAttribute("pens_conceded")
OWN_GOALS = FloatDataAttribute("own_goals")
BALL_RECOVERIES = FloatDataAttribute("ball_recoveries")
AERIALS_WON = FloatDataAttribute("aerials_won")
AERIALS_LOST = FloatDataAttribute("aerials_lost")


TOUCHES = FloatDataAttribute("touches")
TOUCHES_DEF_PEN_AREA = FloatDataAttribute("touches_def_pen_area")
TOUCHES_DEF_3RD = FloatDataAttribute("touches_def_3rd")
TOUCHES_MID_3RD = FloatDataAttribute("touches_mid_3rd")
TOUCHES_ATT_3RD = FloatDataAttribute("touches_att_3rd")
TOUCHES_ATT_PEN_AREA = FloatDataAttribute("touches_att_pen_area")
TOUCHES_LIVE_BALL = FloatDataAttribute("touches_live_ball")
DRIBBLES_COMPLETED = FloatDataAttribute("dribbles_completed")
DRIBBLES = FloatDataAttribute("dribbles")

PLAYERS_DRIBBLED_PAST = FloatDataAttribute("players_dribbled_past")
NUTMEGS = FloatDataAttribute("nutmegs")
CARRIES = FloatDataAttribute("carries")
CARRY_DISTANCE = FloatDataAttribute("carry_distance")
CARRY_PROGRESSIVE_DISTANCE = FloatDataAttribute("carry_progressive_distance")
PROGRESSIVE_CARRIES = FloatDataAttribute("progressive_carries")
CARRIES_INTO_FINAL_THIRD = FloatDataAttribute("carries_into_final_third")
CARRIES_INTO_PENALTY_AREA = FloatDataAttribute("carries_into_penalty_area")
MISCONTROLS = FloatDataAttribute("miscontrols")
DISPOSSESSED = FloatDataAttribute("dispossessed")
PASS_TARGETS = FloatDataAttribute("pass_targets")
PASSES_RECEIVED = FloatDataAttribute("passes_received")

PROGRESSIVE_PASSES_RECEIVED = FloatDataAttribute("progressive_passes_received")

GOALS = FloatDataAttribute("goals")
ASSISTS = FloatDataAttribute("assists")
PENS_MADE = FloatDataAttribute("pens_made")
PENS_ATT = FloatDataAttribute("pens_att")
SHOTS_TOTAL = FloatDataAttribute("shots_total")
SHOTS_ON_TARGET = FloatDataAttribute("shots_on_target")
CARDS_YELLOW = FloatDataAttribute("cards_yellow")
CARDS_RED = FloatDataAttribute("cards_red")
TOUCHES = FloatDataAttribute("touches")
PRESSURES = FloatDataAttribute("pressures")
TACKLES = FloatDataAttribute("tackles")
INTERCEPTIONS = FloatDataAttribute("interceptions")
BLOCKS = FloatDataAttribute("blocks")
XG = FloatDataAttribute("xg")
NPXG = FloatDataAttribute("npxg")
XA = FloatDataAttribute("xa")
SCA = FloatDataAttribute("sca")
GCA = FloatDataAttribute("gca")
PASSES_COMPLETED = FloatDataAttribute("passes_completed")
PASSES = FloatDataAttribute("passes")

PROGRESSIVE_PASSES = FloatDataAttribute("progressive_passes")
CARRIES = FloatDataAttribute("carries")
PROGRESSIVE_CARRIES = FloatDataAttribute("progressive_carries")
DRIBBLES_COMPLETED = FloatDataAttribute("dribbles_completed")
DRIBBLES = FloatDataAttribute("dribbles")

YEAR_FB_REF = IntDataAttribute(
    "year", rename_to="season", agg_function="first", immutable=True
)

SHOTS_ON_TARGET_AGAINST = FloatDataAttribute("shots_on_target_against")
GOALS_AGAINST_GK = FloatDataAttribute("goals_against_gk")
SAVES = FloatDataAttribute("saves")
SAVE_PCT = FloatDataAttribute("save_pct")
CLEAN_SHEETS = FloatDataAttribute("clean_sheets")
PSXG_GK = FloatDataAttribute("psxg_gk")
PENS_ATT_GK = FloatDataAttribute("pens_att_gk")
PENS_ALLOWED = FloatDataAttribute("pens_allowed")
PENS_SAVED = FloatDataAttribute("pens_saved")
PENS_MISSED_GK = FloatDataAttribute("pens_missed_gk")
PASSES_COMPLETED_LAUNCHED_GK = FloatDataAttribute("passes_completed_launched_gk")
PASSES_LAUNCHED_GK = FloatDataAttribute("passes_launched_gk")
PASSES_PCT_LAUNCHED_GK = FloatDataAttribute("passes_pct_launched_gk")
PASSES_GK = FloatDataAttribute("passes_gk")
PASSES_THROWS_GK = FloatDataAttribute("passes_throws_gk")
PCT_PASSES_LAUNCHED_GK = FloatDataAttribute("pct_passes_launched_gk")
PASSES_LENGTH_AVG_GK = FloatDataAttribute("passes_length_avg_gk")
GOAL_KICKS = FloatDataAttribute("goal_kicks")
PCT_GOAL_KICKS_LAUNCHED = FloatDataAttribute("pct_goal_kicks_launched")
GOAL_KICK_LENGTH_AVG = FloatDataAttribute("goal_kick_length_avg")
CROSSES_GK = FloatDataAttribute("crosses_gk")
CROSSES_STOPPED_GK = FloatDataAttribute("crosses_stopped_gk")
CROSSES_STOPPED_PCT_GK = FloatDataAttribute("crosses_stopped_pct_gk")
DEF_ACTIONS_OUTSIDE_PEN_AREA_GK = FloatDataAttribute("def_actions_outside_pen_area_gk")
AVG_DISTANCE_DEF_ACTIONS_GK = FloatDataAttribute("avg_distance_def_actions_gk")

KEEPER_DATA_SETS = {
    KEEPER_DATA: [
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        SHOTS_ON_TARGET_AGAINST,
        GOALS_AGAINST_GK,
        SAVES,
        SAVE_PCT,
        CLEAN_SHEETS,
        PSXG_GK,
        PENS_ATT_GK,
        PENS_ALLOWED,
        PENS_SAVED,
        PENS_MISSED_GK,
        PASSES_COMPLETED_LAUNCHED_GK,
        PASSES_LAUNCHED_GK,
        PASSES_PCT_LAUNCHED_GK,
        PASSES_GK,
        PASSES_THROWS_GK,
        PCT_PASSES_LAUNCHED_GK,
        PASSES_LENGTH_AVG_GK,
        GOAL_KICKS,
        PCT_GOAL_KICKS_LAUNCHED,
        GOAL_KICK_LENGTH_AVG,
        CROSSES_GK,
        CROSSES_STOPPED_GK,
        CROSSES_STOPPED_PCT_GK,
        DEF_ACTIONS_OUTSIDE_PEN_AREA_GK,
        AVG_DISTANCE_DEF_ACTIONS_GK,
    ]
}

DATA_SETS = {
    DEFENSE_DATA: [
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        TACKLES,
        TACKLES_WON,
        TACKLES_DEF_3RD,
        TACKLES_MID_3RD,
        TACKLES_ATT_3RD,
        DRIBBLE_TACKLES,
        DRIBBLES_VS,
        DRIBBLED_PAST,
        PRESSURES,
        PRESSURE_REGAINS,
        PRESSURES_DEF_3RD,
        PRESSURES_MID_3RD,
        PRESSURES_ATT_3RD,
        BLOCKS,
        BLOCKED_SHOTS,
        BLOCKED_SHOTS_SAVES,
        BLOCKED_PASSES,
        INTERCEPTIONS,
        TACKLES_INTERCEPTIONS,
        CLEARANCES,
        ERRORS,
        BENCH_EXPLAIN,
    ],
    GCA_DATA: [
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        SCA,
        SCA_PASSES_LIVE,
        SCA_PASSES_DEAD,
        SCA_DRIBBLES,
        SCA_SHOTS,
        SCA_FOULED,
        SCA_DEFENSE,
        GCA,
        GCA_PASSES_LIVE,
        GCA_PASSES_DEAD,
        GCA_DRIBBLES,
        GCA_SHOTS,
        GCA_FOULED,
        GCA_DEFENSE,
        BENCH_EXPLAIN,
    ],
    PASSING_DATA: [
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        PASSES_COMPLETED,
        PASSES,
        PASSES_TOTAL_DISTANCE,
        PASSES_PROGRESSIVE_DISTANCE,
        PASSES_COMPLETED_SHORT,
        PASSES_SHORT,
        PASSES_COMPLETED_MEDIUM,
        PASSES_MEDIUM,
        PASSES_COMPLETED_LONG,
        PASSES_LONG,
        ASSISTS,
        XA,
        ASSISTED_SHOTS,
        PASSES_INTO_FINAL_THIRD,
        PASSES_INTO_PENALTY_AREA,
        CROSSES_INTO_PENALTY_AREA,
        PROGRESSIVE_PASSES,
        BENCH_EXPLAIN,
        YEAR_FB_REF,
    ],
    MISC_DATA: {
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        CARDS_YELLOW,
        CARDS_RED,
        CARDS_YELLOW_RED,
        FOULS,
        FOULED,
        OFFSIDES,
        CROSSES,
        INTERCEPTIONS,
        TACKLES_WON,
        PENS_WON,
        PENS_CONCEDED,
        OWN_GOALS,
        BALL_RECOVERIES,
        AERIALS_WON,
        AERIALS_LOST,
        BENCH_EXPLAIN,
        YEAR_FB_REF,
    },
    PASSING_TYPES_DATA: [
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        PASSES,
        PASSES_LIVE,
        PASSES_DEAD,
        PASSES_FREE_KICKS,
        THROUGH_BALLS,
        PASSES_PRESSURE,
        PASSES_SWITCHES,
        CROSSES,
        CORNER_KICKS,
        CORNER_KICKS_IN,
        CORNER_KICKS_OUT,
        CORNER_KICKS_STRAIGHT,
        PASSES_GROUND,
        PASSES_LOW,
        PASSES_HIGH,
        PASSES_LEFT_FOOT,
        PASSES_RIGHT_FOOT,
        PASSES_HEAD,
        THROW_INS,
        PASSES_OTHER_BODY,
        PASSES_COMPLETED,
        PASSES_OFFSIDES,
        PASSES_OOB,
        PASSES_INTERCEPTED,
        PASSES_BLOCKED,
        BENCH_EXPLAIN,
        YEAR_FB_REF,
    ],
    POSSESSION_DATA: [
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        TOUCHES,
        TOUCHES_DEF_PEN_AREA,
        TOUCHES_DEF_3RD,
        TOUCHES_MID_3RD,
        TOUCHES_ATT_3RD,
        TOUCHES_ATT_PEN_AREA,
        TOUCHES_LIVE_BALL,
        DRIBBLES_COMPLETED,
        DRIBBLES,
        PLAYERS_DRIBBLED_PAST,
        NUTMEGS,
        CARRIES,
        CARRY_DISTANCE,
        CARRY_PROGRESSIVE_DISTANCE,
        PROGRESSIVE_CARRIES,
        CARRIES_INTO_FINAL_THIRD,
        CARRIES_INTO_PENALTY_AREA,
        MISCONTROLS,
        DISPOSSESSED,
        PASS_TARGETS,
        PASSES_RECEIVED,
        PROGRESSIVE_PASSES_RECEIVED,
        BENCH_EXPLAIN,
        YEAR_FB_REF,
    ],
    SUMMARY_DATA: [
        DAY_OF_WEEK,
        COMPETITION,
        ROUND,
        VENUE,
        RESULT,
        TEAM,
        OPPONENT,
        STARTED,
        POSITION,
        MINUTES,
        GOALS,
        ASSISTS,
        PENS_MADE,
        PENS_ATT,
        SHOTS_TOTAL,
        SHOTS_ON_TARGET,
        CARDS_YELLOW,
        CARDS_RED,
        TOUCHES,
        PRESSURES,
        TACKLES,
        INTERCEPTIONS,
        BLOCKS,
        XG,
        NPXG,
        XA,
        SCA,
        GCA,
        PASSES_COMPLETED,
        PASSES,
        PROGRESSIVE_PASSES,
        CARRIES,
        PROGRESSIVE_CARRIES,
        DRIBBLES_COMPLETED,
        DRIBBLES,
        BENCH_EXPLAIN,
        YEAR_FB_REF,
    ],
}

ALL_DATA_SETS = DATA_SETS
ALL_DATA_SETS.update(KEEPER_DATA_SETS)
