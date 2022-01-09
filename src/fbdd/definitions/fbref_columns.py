from fbdd.definitions.core import DateDataAttribute, DiffDerivedAttribute, FloatDataAttribute, IntDataAttribute, PctDerivedAttribute, RatioDerivedAttribute, StrDataAttribute
from fbdd.definitions.core import list_all_values


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
PASSES_COMPLETED_LAUNCHED_GK = FloatDataAttribute(
    "passes_completed_launched_gk")
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
DEF_ACTIONS_OUTSIDE_PEN_AREA_GK = FloatDataAttribute(
    "def_actions_outside_pen_area_gk")
AVG_DISTANCE_DEF_ACTIONS_GK = FloatDataAttribute("avg_distance_def_actions_gk")


SHOT_PCT = PctDerivedAttribute("shot_pct", SHOTS_ON_TARGET, SHOTS_TOTAL)
XG_PER_SHOT = RatioDerivedAttribute("xg_per_shot", XG, SHOTS_TOTAL)
XG_OUTPERFORM = DiffDerivedAttribute("xg_outperform", GOALS, XG)
NON_PENALTY_GOALS = DiffDerivedAttribute("non_penalty_goals", GOALS, PENS_MADE)
SCA_LIVE = DiffDerivedAttribute("sca_live", SCA, SCA_PASSES_DEAD)
NPXG_PER_SHOT = RatioDerivedAttribute("npxg_per_shot", NPXG, SHOTS_TOTAL)
NPXG_OUTPERFORM = DiffDerivedAttribute(
    "npxg_outperform", NON_PENALTY_GOALS, NPXG)
NPXG_OUTPERFORM_PER_SHOT = RatioDerivedAttribute(
    "npxg_outperfor_per_shot", NPXG_OUTPERFORM, SHOTS_TOTAL
)
NON_PENALTY_GOALS_PER_SHOT = RatioDerivedAttribute(
    "npg_per_shot", NON_PENALTY_GOALS, SHOTS_TOTAL
)
