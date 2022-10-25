from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "pingpong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pingpong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "pingpong/assets/sounds/boing.wav"
WELCOME_SOUND = "pingpong/assets/sounds/start.wav"
OVER_SOUND = "pingpong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "pingpong/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "LEVEL"
SCORE_GROUP = "SCORE"
LEVEL_FORMAT = "LEVEL: {}"
SCORE_FORMAT = "VOLLEYS: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pingpong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"pingpong/assets/images/{n:03}.png" for n in range(100, 103)], [f"pingpong/assets/images/{n:03}.png" for n in range(103, 106)]
# RACKET_IMAGES1 = [f"pingpong/assets/images/{n:03}.png" for n in range(103, 106)]
RACKET_WIDTH = 30
RACKET_HEIGHT = 100
RACKET_RATE = 7
RACKET_VELOCITY = 8


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"