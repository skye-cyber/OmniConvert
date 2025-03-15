import os

from colorama import Fore, Style, init

init(autoreset=True)

if os.name == "posix":
    RESET = '\033[0m'  # Reset to default text color

    RED = '\033[91m'  # Normal RED
    DRED = '\033[1;91m'  # Deep RED
    FRED = '\033[2;91m'  # Faint red
    IRED = '\033[3;91m'  # Indented RED

    GREEN = '\033[92m'  # Normal green
    DGREEN = '\033[1;92m'  # Deep green
    FGREEN = '\033[2;92m'  # Faint green
    IGREEN = '\033[3;92m'  # Indented GREEN

    YELLOW = '\033[93m'  # Normal yellow
    DYELLOW = '\033[1;93m'  # Deep YELLOW
    FYELLOW = '\033[2;93m'  # Faint YELLOW
    IYELLOW = '\033[3;93m'  # Indented YELLOW

    BLUE = '\033[94m'  # Normal BLUE
    DBLUE = '\033[1;94m'  # Deep BLUE
    FBLUE = '\033[2;94m'  # Faint Blue
    IBLUE = '\033[3;94m'  # Indented BLUE

    MAGENTA = '\033[95m'  # Normal MAGENTA
    DMAGENTA = '\033[1;95m'  # Deep MAGENTA
    FMAGENTA = '\033[2;95m'  # Faint MAGENTA
    IMAGENTA = '\033[3;95m'

    CYAN = '\033[96m'  # Normal cyan
    DCYAN = '\033[1;96m'  # Deep CYAN
    FCYAN = '\033[2;96m'  # Faint cyan
    ICYAN = '\033[3;96m'  # Indented CYAN

    BWHITE = '\033[1m'  # Bold white
    BBWHITE = '\033[5;97;1m'  # Bold Blinking white

elif os.name == "nt":
    RESET = Style.RESET_ALL

    RED = Fore.LIGHTRED_EX
    DRED = Fore.RED
    FRED = Fore.RED
    IRED = Fore.RED

    GREEN = Fore.LIGHTGREEN_EX
    DGREEN = Fore.GREEN
    FGREEN = Fore.GREEN
    IGREEN = Fore.GREEN

    YELLOW = Fore.LIGHTYELLOW_EX
    FYELLOW = Fore.YELLOW
    DYELLOW = Fore.YELLOW
    IYELLOW = Fore.YELLOW

    BLUE = Fore.LIGHTBLUE_EX
    DBLUE = Fore.BLUE
    FBLUE = Fore.BLUE
    IBLUE = Fore.BLUE

    MAGENTA = Fore.LIGHTMAGENTA_EX
    DMAGENTA = Fore.MAGENTA
    IMAGENTA = Fore.LIGHTMAGENTA_EX
    FMAGENTA = Fore.MAGENTA

    CYAN = Fore.LIGHTCYAN_EX
    DCYAN = Fore.CYAN
    ICYAN = Fore.WHITE
    FCYAN = Fore.CYAN

    BWHITE = Fore.WHITE
    BBWHITE = Fore.WHITE

# return RESET, RED, DRED, GREEN, DGREEN, YELLOW, DYELLOW, BLUE, DBLUE,
# MAGENTA, DMAGENTA, CYAN, DCYAN
