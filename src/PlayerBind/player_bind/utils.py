from mcdreforged.api.all import *


psi = ServerInterface.psi()
builder = SimpleCommandBuilder()

MCDRConfig = psi.get_mcdr_config()
serverDir = MCDRConfig["working_directory"]