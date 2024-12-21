import re

from matrix_sync.commands import matrix_reporter # type: ignore
from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, old):
    server.logger.info("Subpack of MatrixSync: [MSync]PlayingTips loaded.")

def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    tip = f"[+]{player}"
    matrix_reporter(tip)

def on_player_left(server: PluginServerInterface, player: str):
    tip = f"[-]{player}"
    matrix_reporter(tip)

def on_info(server: PluginServerInterface, info: Info):
    if info.is_from_server and re.fullmatch(r'(.+) issued server command: (.+)', info.content):
        match = re.fullmatch(r'(.+) issued server command: (.+)', info.content)
        if match:
            player = match.group(1)
            command = match.group(2)
        server.say(f"[!] {player} 执行游戏指令: {command}")
        matrix_reporter(f"[!] {player} 执行游戏指令: {command}")
