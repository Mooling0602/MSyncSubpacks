import re

from matrix_sync.commands import matrix_reporter # type: ignore
from mcdreforged.api.all import *

psi = ServerInterface.psi()

def on_load(server: PluginServerInterface, old):
    server.logger.info("Subpack of MatrixSync: [Msync]MoreMessages loaded.")

def on_user_info(server: PluginServerInterface, info: Info):
    msg = formatter(info)
    if msg is not None:
        matrix_reporter(msg)


def formatter(info: Info):
    msg = None
    if info.player is None:
        if re.fullmatch(r'say \S*', info.content):
            msg_content = '{}'.format(info.content.rsplit(' ', 1)[1])
            msg = f"<Console> {msg_content}"
        else:
            msg = f"[!] Console execute command: {info.content}"
        if info.content == "stop":
            msg = "[!] Stopping server from console..."
    else:
        if info.content.startswith("!!"):
            msg = f"[!] {info.player} execute MCDR command: {info.content}"
        else:
            msg = None
    return msg