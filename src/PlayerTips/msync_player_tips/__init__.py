from matrix_sync.commands import matrix_reporter # type: ignore
from mcdreforged.api.all import *


default_config = {
    "on_joined": "[+]%player%",
    "on_left": "[-]%player%"
}

def on_load(server: PluginServerInterface, old):
    global config
    config = server.load_config_simple(file_name='config/matrix_sync/player_tips/config.json', default_config=default_config, in_data_folder=False)
    server.logger.info("§a+§r [MSync]PlayerTips")

def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    tip = config["on_joined"].replace('%player%', player)
    matrix_reporter(tip)

def on_player_left(server: PluginServerInterface, player: str):
    tip = config["on_left"].replace('%player%', player)
    matrix_reporter(tip)

def on_unload(server: PluginServerInterface):
    server.logger.info("§c-§r [MSync]PlayerTips")