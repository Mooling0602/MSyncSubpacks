import re

from typing import Optional
from .utils import *


def rcon_error() -> bool:
    psi.logger.error("Rcon worked wrong!")
    return False

def rcon_error_log(log: str) -> bool:
    psi.logger.error(f"Failed for unknown error: {log}")
    return False

def add_whitelist(player: str, floodgate: Optional[bool]=False):
    if not floodgate:
        resp = psi.rcon_query(f"whitelist add {player}")
        if resp is None:
            return rcon_error()
        else:
            if resp == "Player is already whitelisted":
                return True
            elif re.fullmatch(r"Added .+ to the whitelist", resp):
                return True
            elif resp == "That player does not exist":
                psi.logger.error("Invaild player name!")
                return False
            else:
                rcon_error_log(resp)
    else:
        psi.execute(f"fwhitelist add {player}")
        return "Please wait for any response for rcon not supported here..."

def remove_whitelist(player: str, floodgate: Optional[bool]=False):
    if not floodgate:
        resp = psi.rcon_query(f"whitelist remove {player}")
        if resp is None:
            return rcon_error()
        else:
            if resp == "Player is not whitelisted":
                psi.logger.warning("Invaild player name")
                return False
            elif re.fullmatch(r"Removed .+ from the whitelist", resp):
                return True
            else:
                rcon_error_log(resp)
    else:
        psi.execute(f"fwhitelist remove {player}")
        return "Please wait for any response for rcon not supported here..."
        