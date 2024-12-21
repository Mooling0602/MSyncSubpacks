from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, old):
    server.logger.info("Subpack of MatrixSync: [MSync]plgDebugger loaded.")
    server.register_event_listener('MatrixRoomMessage', main)

def main(server: PluginServerInterface, message: str, sender: str, room_name):
    server.logger.info(f"Content: {message}")
    server.logger.info(f"Sender: {sender}")
    if room_name is not None:
        server.logger.info(f"Room Name: {room_name}")