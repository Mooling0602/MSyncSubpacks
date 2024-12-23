import re

from matrix_sync.commands import matrix_reporter # type: ignore
from mcdreforged.api.all import *
from .config import load_config


psi = ServerInterface.psi()

config = None

def on_load(server: PluginServerInterface, old):
    global config
    server.logger.info("§a+§r [Msync]CommandMessages")
    config = load_config(server)

def on_user_info(server: PluginServerInterface, info: Info):
    msg = formatter(info)
    if msg is not None and msg != "":
        matrix_reporter(msg)

def formatter(info: Info):
    msg = None
    if info.player is None:
        if re.fullmatch(r'say \S*', info.content):
            message = '{}'.format(info.content.rsplit(' ', 1)[1])
            msg = config["on_console"]["on_chat"].replace('%message%', message)
        else:
            msg = config["on_console"]["on_command"].replace('%command%', info.content)
        if info.content == "stop":
            msg = config["on_console"]["on_stop_command"]
    else:
        if info.content.startswith("!!"):
            msg = config["on_player"]["on_mcdr_command"].replace('%player%', info.player).replace('%command%', info.content)
        else:
            msg = None
    return msg

def on_info(server: PluginServerInterface, info: Info):
    if info.is_from_server and re.fullmatch(r'(.+) issued server command: (.+)', info.content):
        match = re.fullmatch(r'(.+) issued server command: (.+)', info.content)
        if match:
            player = match.group(1)
            command = match.group(2)
        msg = config["on_player"]["on_server_command"]["content"].replace('%player%', player).replace('%command%', command)
        if msg is not None and msg != "":
            if config["on_player"]["on_server_command"]["broadcast_online"]:
                server.say(msg)
            matrix_reporter(msg)

def on_unload(server: PluginServerInterface):
    server.logger.info("§c-§r [MSync]CommandMessages")