from colorama import Fore, Style
from typing import Literal
import os

type menu_response_type = tuple[Literal["exit"]] | tuple[Literal["invalid-response"]] | tuple[Literal["config"]] | tuple[Literal["create-file"], FilePayload]
type config_response_type = Literal["exit"] | Literal["fail-apply"] | Literal["sucess-apply"]

TARGET_FOLDER_PATH = path = os.getcwd()
SRC_PATH_FOLDER = os.path.dirname(os.path.abspath(__file__))
CONSTRUCTOR_PATH_FOLDER = os.path.dirname(SRC_PATH_FOLDER)

class Colors:
    GREEN = Fore.GREEN
    RESET = Style.RESET_ALL
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    LIGHT_CYAN = Fore.LIGHTCYAN_EX
    MAGENTA = Fore.LIGHTMAGENTA_EX