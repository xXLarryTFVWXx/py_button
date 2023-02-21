import sys, curses, string
from curses import wrapper

VER: float=0.1

HELP_SWITCHES: tuple=(
    "-h",
    "--help",
    "/?",
    "/h",
    "/help",
    "-?"
)

VERSION_SWITCHES: tuple=(
    "-v",
    "-ver",
    "--version"
)

class Button:
    def __init__(self, console, x, y, color, text):
        self.x = x
        self.y = y
        self.console = console
        self.color = color
        self.hover_color = color #  Will invert when I figure out how to do this.
        self.text: str = text
        self.width = len(text) + 2
        self.text.center(self.width)
    def render(self, mouse_position, mouse_clicked):
        self.console.addstr(self.y, self.x, " "*self.width, self.color)
        self.console.addstr(self.y+1, self.x, self.text, self.color)
        self.console.addstr(self.y+2, self.x, " "*self.width, self.color)
        if mouse_info[0] in range(self.x, self.x+self.width):
            if mouse_info[1] in range(self.y, self.y+3):
                if mouse

HELP_MESSAGE: list[str]=[
    f"Python button supplement version {VER} by xXLarryTFVWXx",
    "This is a port of KVC's Button function to python curses because Microsoft broke something.",
    "",
    "This supplementary script adds the ability to use clickable buttons to your batch programs.",
    "",
    f"Syntax: py py_button.py [{' | '.join(HELP_SWITCHES)}]"
]

def is_string_dirty(string_to_test: str=""):
    string_is_dirty: bool=False
    for character in string.punctuation:
        string_is_dirty = string_to_test.find(character) != -1
    return string_is_dirty

colors = []

def generate_buttons():
    """This generates the buttons"""
    button_list = []
    x = y = 0 
    color = []
    text = ""
    width = 0
    for index, argument in arguments: # Iterate over each argument getting the remainder of 4 from each argument
        modulo = index % 4
        if modulo == 0: # X coordinate
            x: int = int(argument)
        elif modulo == 1: # Y coordinate
            y: int = int(argument)
        elif modulo == 2: # color will need converted at some point to curses color pallete
            color: list[str] = [_ for _ in argument]
        else: # This has to be the text for the button.
            text: str = argument
            button_list.append([x, y, color, text])
            x = y = 0
            color = []
            text = ""

    return button_list

def main(stdscr):
    button_list = generate_buttons()
    mouse_down = False
    index = 2**32-2
    while not mouse_down:
        """display buttons here."""
        for index, button in button_list:
            mouse_pos = (0,0)
            mouse_clicked = False
            if curses.getch() == curses.KEY_MOUSE:
                mouse_info = curses.getmouse()
                mouse_pos = mouse_info[1:3]
                mouse_down = mouse_info[-1] == curses.BUTTON1_CLICKED
            if mouse_down:
                break
    else:
        sys.exit(index+1)




if __name__ == "__main__":
    arguments = sys.argv[1::]
    if len(sys.argv) == 1 or sys.argv[1] in HELP_SWITCHES:
        print(*HELP_MESSAGE, sep=[str]"\n")
    elif arguments[0] in VERSION_SWITCHES:
        print(VER)
    else:
        wrapper(main)
