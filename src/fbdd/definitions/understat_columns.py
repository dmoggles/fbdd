from fbdd.definitions import core
from fbdd.definitions.understat import TEAM_RENAMES
import pandas as pd
ID = core.IntDataAttribute('id', immutable=True)
MINUTE = core.IntDataAttribute('minute', immutable=True)
RESULT = core.StrDataAttribute('result')
X = core.FloatDataAttribute('X', agg_function="mean", immutable=True)
Y = core.FloatDataAttribute('Y', agg_function="mean", immutable=True)
XG = core.FloatDataAttribute('xG', agg_function="sum", immutable=True)
PLAYER = core.StrDataAttribute('player')
HOME_OR_AWAY = core.StrDataAttribute('h_a')
PLAYER_ID = core.IntDataAttribute('player_id', immutable=True)
SITUATION = core.StrDataAttribute('situation')
YEAR = core.IntDataAttribute('season', immutable=True)
SHOT_TYPE= core.StrDataAttribute('shotType')
MATCH_ID= core.IntDataAttribute('match_id', immutable=True)
HOME_TEAM= core.StrDataAttribute('h_team')
AWAY_TEAM= core.StrDataAttribute('a_team')
HOME_GOALS= core.IntDataAttribute('h_goals', immutable=True)
AWAY_GOALS= core.IntDataAttribute('a_goals', immutable=True)
DATE=core.DateDataAttribute('date', transform_function=lambda x: pd.Timestamp(x).date())
PLAYER_ASSISTED=core.StrDataAttribute('player_assisted')
LAST_ACTION=core.StrDataAttribute('lastAction')


PLAYER_TEAM = core.LambdaDerivedAttribute('player_team','str','first', lambda r: r[HOME_TEAM.N] if r[HOME_OR_AWAY.N] == 'h' else r[AWAY_TEAM.N])