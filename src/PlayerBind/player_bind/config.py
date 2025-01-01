import os
from .utils import serverDir


exists_floodgate = False
if os.path.exists(f"{serverDir}/plugins/floodgate/key.pem"):
    exists_floodgate = True

default_config = {
    "online_mode": True,
    "floodgate": exists_floodgate
}