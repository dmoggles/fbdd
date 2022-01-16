from enum import Enum
TEAM_RENAMES = {
    'Leeds': 'Leeds United',
    'Leicester':   'Leicester City',
    'Manchester United': 'Manchester Utd',
    'Newcastle United': 'Newcastle Utd',
    'Norwich': 'Norwich City',
}

class LastAction(Enum):
    AERIAL="Aerial"
    PASS="Pass"
    TAKE_ON="TakeOn"
    NONE="None"
    BALL_RECOVERY="BallRecovery"
    CHIPPED="Chipped"
    CROSS="Cross"
    REBOUND="Rebound"
    THROUGHBALL="Throughball"
    DISPOSSESSED="Dispossessed"
    STANDARD="Standard"
    HEAD_PASS="HeadPass"
    BALL_TOUCH="BallTouch"
    TACKLE="Tackle"
    LAY_OFF="LayOff"
    CORNER_AWARDED="CornerAwarded"
    INTERCEPTION="Interception"
    END="End"
    BLOCKED_PASS="BlockedPass"
    FOUL="Foul"
    SUBSTITUTION_ON="SubstitutionOn"
    CHALLENGE="Challenge"
    CLEARANCE="Clearance"
    GOAL="Goal"
    CARD="Card"
    OFFSIDE_PASS="OffsidePass"
    KEEPER_PICKUP="KeeperPickup"
    SAVE="Save"

class Situation(Enum):
    OPEN_PLAY="OpenPlay"
    FROM_CORNER="FromCorner"
    SET_PIECE="SetPiece"
    PENALTY="Penalty"
    DIRECT_FREEKICK="DirectFreekick"

class ShotType(Enum):
    HEAD="Head"
    LEFT_FOOT="LeftFoot"
    RIGHT_FOOT="RightFoot"
    OTHER_BODY_PART="OtherBodyPart"