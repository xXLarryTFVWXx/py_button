import sys, curses
from curses import wrapper
import typing

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

help_msg: list=[
    f"Python button supplement version {VER} by xXLarryTFVWXx",
    "This is a port of KVC's Button function to python curses because Microsoft broke something.",
    "",
    "This supplementary script adds the ability to use clickable buttons to your batch programs.",
    "",
    f"Syntax: py py_button.py [{' | '.join(HELP_SWITCHES)}]"
]

def helper():
    print(*help_msg, sep="\n")

def main(stdscr):
    button_list: list[tuple[int, int, str, str]] = []
    button_info = []
    arguments = sys.argv[1::]
    for index, item in enumerate(arguments):
        remainder = index % 4
        if remainder == 0:
            if type(item) == str:
                if item.lower() == 'x':
                    # print(f'{remainder}|{item}')
                    break
            if not button_info == []:
                button_list.append(button_info)
            button_info = []
        if remainder < 2:
            button_info.append(int(item))
        elif remainder == 2:
            button_info.append(int(item, base=16))
        else:
            button_info.append(item)
    print(button_list)



if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] in HELP_SWITCHES:
        helper()
    elif sys.argv[1] in VERSION_SWITCHES:
        print(VER)
    else:
        wrapper(main)
