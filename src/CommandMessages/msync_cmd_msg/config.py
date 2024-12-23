from mcdreforged.api.all import *


MCDRLocale = ServerInterface.psi().get_mcdr_language()

default_config = {
    "on_console": {
        "on_chat": "<Console> %message%",
        "on_command": "[!] Console execute command: %command%",
        "on_stop_command": "An admin or preset automated task has shut down the server from the console."
    },
    "on_player": {
        "on_mcdr_command": "[!] %player% execute MCDR command: %command%",
        "on_server_command": {
            "content": "[!] %player%execute server command: %command%",
            "broadcast_online": True
        }
    }
}

default_config_cns = {
    "on_console": {
        "on_chat": "<控制台> %message%",
        "on_command": "[!] 控制台执行命令：%command%",
        "on_stop_command": "管理员或自动化程序任务从控制台关闭了服务器。"
    },
    "on_player": {
        "on_mcdr_command": "[!] %player%执行MCDR命令：%command%",
        "on_server_command": {
            "content": "[!] %player%执行服务器命令：%command%",
            "broadcast_online": True
        }
    }
}

def load_config(server: PluginServerInterface):
    if MCDRLocale == "zh_cn":
        return server.load_config_simple(file_name='config/matrix_sync/cmd_msg/config.json', default_config=default_config_cns, in_data_folder=False)
    else:
        return server.load_config_simple(file_name='config/matrix_sync/cmd_msg/config.json', default_config=default_config, in_data_folder=False)