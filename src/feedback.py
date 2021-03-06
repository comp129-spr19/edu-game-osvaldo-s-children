from pygame import (
    rect,

    display
)

from pygame.font import (
    # class objects
    Font,

    SysFont,
    init
)

from text_box import (
    TextBox
)

from system_utils import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

# initialize font environment
init()

# class constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

MAX_CHARS = 80
# TODO: Increase font size after implementing multi-line feedback
FONT = SysFont('Arial', 20, bold=True)

# feedback global variables
text_boxes = None


def __init__():
    global text_boxes

    text_boxes = []


def on_init():
    pass


def show_pos_feedback(string):
    _show_feedback(string, BLACK, GREEN)


def show_neg_feedback(string):
    _show_feedback(string, BLACK, RED)


def show_info_feedback(string):
    _show_feedback(string, BLACK, YELLOW)


def _show_feedback(string, text_color, box_color):
    text = FONT.render(string, True, text_color, box_color)
    tb = TextBox(box_color, text)
    text_boxes.append(tb)


def on_render(surface):
    # TODO dynamically place text boxes
    for text_box in text_boxes:
        if not text_box.on_render(surface):
            text_boxes.remove(text_box)
