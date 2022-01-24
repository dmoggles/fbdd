from fbdd.definitions import core
from fbdd.definitions.understat import TEAM_RENAMES
import pandas as pd
ID = core.IntDataAttribute('id', immutable=True, source=core.DataSources.UNDERSTAT)
MINUTE = core.IntDataAttribute('minute', immutable=True, source=core.DataSources.UNDERSTAT)
RESULT = core.StrDataAttribute('result', source=core.DataSources.UNDERSTAT)
X = core.FloatDataAttribute('X', agg_function="mean", immutable=True, source=core.DataSources.UNDERSTAT)
Y = core.FloatDataAttribute('Y', agg_function="mean", immutable=True, source=core.DataSources.UNDERSTAT)
XG = core.FloatDataAttribute('xG', agg_function="sum", immutable=True, source=core.DataSources.UNDERSTAT)
PLAYER = core.StrDataAttribute('player', source=core.DataSources.UNDERSTAT)
HOME_OR_AWAY = core.StrDataAttribute('h_a', source=core.DataSources.UNDERSTAT)
PLAYER_ID = core.IntDataAttribute('player_id', immutable=True, source=core.DataSources.UNDERSTAT)
SITUATION = core.StrDataAttribute('situation', source=core.DataSources.UNDERSTAT)
YEAR = core.IntDataAttribute('season', immutable=True, source=core.DataSources.UNDERSTAT, agg_function="first")
SHOT_TYPE= core.StrDataAttribute('shotType', source=core.DataSources.UNDERSTAT)
MATCH_ID= core.IntDataAttribute('match_id', immutable=True, source=core.DataSources.UNDERSTAT)
HOME_TEAM= core.StrDataAttribute('h_team', source=core.DataSources.UNDERSTAT)
AWAY_TEAM= core.StrDataAttribute('a_team', source=core.DataSources.UNDERSTAT)
HOME_GOALS= core.IntDataAttribute('h_goals', immutable=True, source=core.DataSources.UNDERSTAT)
AWAY_GOALS= core.IntDataAttribute('a_goals', immutable=True, source=core.DataSources.UNDERSTAT)
DATE=core.DateDataAttribute('date', transform_function=lambda x: pd.Timestamp(x).date(), source=core.DataSources.UNDERSTAT)
PLAYER_ASSISTED=core.StrDataAttribute('player_assisted', source=core.DataSources.UNDERSTAT)
LAST_ACTION=core.StrDataAttribute('lastAction', source=core.DataSources.UNDERSTAT)


PLAYER_TEAM = core.LambdaDerivedAttribute('player_team','str','first', lambda r: r[HOME_TEAM.N] if r[HOME_OR_AWAY.N] == 'h' else r[AWAY_TEAM.N], source=core.DataSources.UNDERSTAT)