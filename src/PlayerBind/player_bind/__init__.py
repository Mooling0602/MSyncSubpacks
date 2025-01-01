from .utils import *
from .config import default_config


def on_load(server: PluginServerInterface, prev_module):
    global cfg
    server.logger.info("§a+§r [MSync]PlayerBind")
    cfg = server.load_config_simple('config.json', default_config)
    if not server.is_rcon_running():
        server.logger.warning("Need rcon enabled!")



