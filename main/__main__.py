import asyncio
import glob
from pathlib import Path
import logging
from . import Drone
from main.utils import load_plugins
from plugins.main import process_queue  # Replace with the actual module name

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Bot Deployed Succesfully")

async def main():
    Drone.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(main(), process_queue()))
