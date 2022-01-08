from fbdd.definitions.core import (
    DateDataAttribute,
    FloatDataAttribute,
    IntDataAttribute,
    StrDataAttribute,
)
import pandas as pd
import itertools
from fbdd.definitions import fbref_columns as fbrc
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


KEEPER_DATA_SETS = {
    KEEPER_DATA: [
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.SHOTS_ON_TARGET_AGAINST,
        fbrc.GOALS_AGAINST_GK,
        fbrc.SAVES,
        fbrc.SAVE_PCT,
        fbrc.CLEAN_SHEETS,
        fbrc.PSXG_GK,
        fbrc.PENS_ATT_GK,
        fbrc.PENS_ALLOWED,
        fbrc.PENS_SAVED,
        fbrc.PENS_MISSED_GK,
        fbrc.PASSES_COMPLETED_LAUNCHED_GK,
        fbrc.PASSES_LAUNCHED_GK,
        fbrc.PASSES_PCT_LAUNCHED_GK,
        fbrc.PASSES_GK,
        fbrc.PASSES_THROWS_GK,
        fbrc.PCT_PASSES_LAUNCHED_GK,
        fbrc.PASSES_LENGTH_AVG_GK,
        fbrc.GOAL_KICKS,
        fbrc.PCT_GOAL_KICKS_LAUNCHED,
        fbrc.GOAL_KICK_LENGTH_AVG,
        fbrc.CROSSES_GK,
        fbrc.CROSSES_STOPPED_GK,
        fbrc.CROSSES_STOPPED_PCT_GK,
        fbrc.DEF_ACTIONS_OUTSIDE_PEN_AREA_GK,
        fbrc.AVG_DISTANCE_DEF_ACTIONS_GK,
    ]
}

DATA_SETS = {
    DEFENSE_DATA: [
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.TACKLES,
        fbrc.TACKLES_WON,
        fbrc.TACKLES_DEF_3RD,
        fbrc.TACKLES_MID_3RD,
        fbrc.TACKLES_ATT_3RD,
        fbrc.DRIBBLE_TACKLES,
        fbrc.DRIBBLES_VS,
        fbrc.DRIBBLED_PAST,
        fbrc.PRESSURES,
        fbrc.PRESSURE_REGAINS,
        fbrc.PRESSURES_DEF_3RD,
        fbrc.PRESSURES_MID_3RD,
        fbrc.PRESSURES_ATT_3RD,
        fbrc.BLOCKS,
        fbrc.BLOCKED_SHOTS,
        fbrc.BLOCKED_SHOTS_SAVES,
        fbrc.BLOCKED_PASSES,
        fbrc.INTERCEPTIONS,
        fbrc.TACKLES_INTERCEPTIONS,
        fbrc.CLEARANCES,
        fbrc.ERRORS,
        fbrc.BENCH_EXPLAIN,
    ],
    GCA_DATA: [
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.SCA,
        fbrc.SCA_PASSES_LIVE,
        fbrc.SCA_PASSES_DEAD,
        fbrc.SCA_DRIBBLES,
        fbrc.SCA_SHOTS,
        fbrc.SCA_FOULED,
        fbrc.SCA_DEFENSE,
        fbrc.GCA,
        fbrc.GCA_PASSES_LIVE,
        fbrc.GCA_PASSES_DEAD,
        fbrc.GCA_DRIBBLES,
        fbrc.GCA_SHOTS,
        fbrc.GCA_FOULED,
        fbrc.GCA_DEFENSE,
        fbrc.BENCH_EXPLAIN,
    ],
    PASSING_DATA: [
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.PASSES_COMPLETED,
        fbrc.PASSES,
        fbrc.PASSES_TOTAL_DISTANCE,
        fbrc.PASSES_PROGRESSIVE_DISTANCE,
        fbrc.PASSES_COMPLETED_SHORT,
        fbrc.PASSES_SHORT,
        fbrc.PASSES_COMPLETED_MEDIUM,
        fbrc.PASSES_MEDIUM,
        fbrc.PASSES_COMPLETED_LONG,
        fbrc.PASSES_LONG,
        fbrc.ASSISTS,
        fbrc.XA,
        fbrc.ASSISTED_SHOTS,
        fbrc.PASSES_INTO_FINAL_THIRD,
        fbrc.PASSES_INTO_PENALTY_AREA,
        fbrc.CROSSES_INTO_PENALTY_AREA,
        fbrc.PROGRESSIVE_PASSES,
        fbrc.BENCH_EXPLAIN,
        fbrc.YEAR_FB_REF,
    ],
    MISC_DATA: {
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.CARDS_YELLOW,
        fbrc.CARDS_RED,
        fbrc.CARDS_YELLOW_RED,
        fbrc.FOULS,
        fbrc.FOULED,
        fbrc.OFFSIDES,
        fbrc.CROSSES,
        fbrc.INTERCEPTIONS,
        fbrc.TACKLES_WON,
        fbrc.PENS_WON,
        fbrc.PENS_CONCEDED,
        fbrc.OWN_GOALS,
        fbrc.BALL_RECOVERIES,
        fbrc.AERIALS_WON,
        fbrc.AERIALS_LOST,
        fbrc.BENCH_EXPLAIN,
        fbrc.YEAR_FB_REF,
    },
    PASSING_TYPES_DATA: [
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.PASSES,
        fbrc.PASSES_LIVE,
        fbrc.PASSES_DEAD,
        fbrc.PASSES_FREE_KICKS,
        fbrc.THROUGH_BALLS,
        fbrc.PASSES_PRESSURE,
        fbrc.PASSES_SWITCHES,
        fbrc.CROSSES,
        fbrc.CORNER_KICKS,
        fbrc.CORNER_KICKS_IN,
        fbrc.CORNER_KICKS_OUT,
        fbrc.CORNER_KICKS_STRAIGHT,
        fbrc.PASSES_GROUND,
        fbrc.PASSES_LOW,
        fbrc.PASSES_HIGH,
        fbrc.PASSES_LEFT_FOOT,
        fbrc.PASSES_RIGHT_FOOT,
        fbrc.PASSES_HEAD,
        fbrc.THROW_INS,
        fbrc.PASSES_OTHER_BODY,
        fbrc.PASSES_COMPLETED,
        fbrc.PASSES_OFFSIDES,
        fbrc.PASSES_OOB,
        fbrc.PASSES_INTERCEPTED,
        fbrc.PASSES_BLOCKED,
        fbrc.BENCH_EXPLAIN,
        fbrc.YEAR_FB_REF,
    ],
    POSSESSION_DATA: [
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.TOUCHES,
        fbrc.TOUCHES_DEF_PEN_AREA,
        fbrc.TOUCHES_DEF_3RD,
        fbrc.TOUCHES_MID_3RD,
        fbrc.TOUCHES_ATT_3RD,
        fbrc.TOUCHES_ATT_PEN_AREA,
        fbrc.TOUCHES_LIVE_BALL,
        fbrc.DRIBBLES_COMPLETED,
        fbrc.DRIBBLES,
        fbrc.PLAYERS_DRIBBLED_PAST,
        fbrc.NUTMEGS,
        fbrc.CARRIES,
        fbrc.CARRY_DISTANCE,
        fbrc.CARRY_PROGRESSIVE_DISTANCE,
        fbrc.PROGRESSIVE_CARRIES,
        fbrc.CARRIES_INTO_FINAL_THIRD,
        fbrc.CARRIES_INTO_PENALTY_AREA,
        fbrc.MISCONTROLS,
        fbrc.DISPOSSESSED,
        fbrc.PASS_TARGETS,
        fbrc.PASSES_RECEIVED,
        fbrc.PROGRESSIVE_PASSES_RECEIVED,
        fbrc.BENCH_EXPLAIN,
        fbrc.YEAR_FB_REF,
    ],
    SUMMARY_DATA: [
        fbrc.DAY_OF_WEEK,
        fbrc.COMPETITION,
        fbrc.ROUND,
        fbrc.VENUE,
        fbrc.RESULT,
        fbrc.TEAM,
        fbrc.OPPONENT,
        fbrc.STARTED,
        fbrc.POSITION,
        fbrc.MINUTES,
        fbrc.GOALS,
        fbrc.ASSISTS,
        fbrc.PENS_MADE,
        fbrc.PENS_ATT,
        fbrc.SHOTS_TOTAL,
        fbrc.SHOTS_ON_TARGET,
        fbrc.CARDS_YELLOW,
        fbrc.CARDS_RED,
        fbrc.TOUCHES,
        fbrc.PRESSURES,
        fbrc.TACKLES,
        fbrc.INTERCEPTIONS,
        fbrc.BLOCKS,
        fbrc.XG,
        fbrc.NPXG,
        fbrc.XA,
        fbrc.SCA,
        fbrc.GCA,
        fbrc.PASSES_COMPLETED,
        fbrc.PASSES,
        fbrc.PROGRESSIVE_PASSES,
        fbrc.CARRIES,
        fbrc.PROGRESSIVE_CARRIES,
        fbrc.DRIBBLES_COMPLETED,
        fbrc.DRIBBLES,
        fbrc.BENCH_EXPLAIN,
        fbrc.YEAR_FB_REF,
    ],
}

ALL_DATA_SETS = DATA_SETS
ALL_DATA_SETS.update(KEEPER_DATA_SETS)