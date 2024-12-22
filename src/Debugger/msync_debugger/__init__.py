from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, old):
    server.logger.info("Subpack of MatrixSync: [MSync]plgDebugger loaded.")
    server.register_event_listener('MatrixRoomMessage', matrix_messages)

def matrix_messages(server: PluginServerInterface, message: str, sender: str, room_id):
    server.logger.info(f"Content: {message}")
    server.logger.info(f"Sender: {sender}")
    server.logger.info(f"Room ID: {room_id}")

def messages_sendto_matrix(server: PluginServerInterface, user_id, room_id):
    server.logger.info(f"Bot: {user_id}")
    server.logger.info(f"Room ID: {room_id}")