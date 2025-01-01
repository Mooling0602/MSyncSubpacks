from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, old):
    server.logger.info("§a+§r [MSync]Debugger")
    server.register_event_listener('MatrixRoomMessage', matrix_messages)

def matrix_messages(server: PluginServerInterface, message, sender, room_info):
    server.logger.info(f"Content: {message}")
    server.logger.info(f"Sender: {sender}")
    server.logger.info(f"Room ID: {room_info.id}")
    server.logger.info(f"Room name: {room_info.display_name}")

def on_unload(server: PluginServerInterface):
    server.logger.info("§c-§r [MSync]Debugger")