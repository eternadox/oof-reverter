import os
import re
import requests
from glob import glob

ROBLOXDIR = os.getenv("LOCALAPPDATA")+"\Roblox\Versions\*"

roblox_versions = glob(ROBLOXDIR, recursive = True)

### Cleaning up versions ###

for v in roblox_versions:
    if (not re.search("version-", v)):
        roblox_versions.pop(roblox_versions.index(v))
        print("[OofReverter] Removed non-version from list of versions: "+v)

for v in roblox_versions:
    if (not os.path.exists(v+"\content\sounds\ouch.ogg")):
        print(f"[OofReverter] Removed version {v} with no oof sound file from list.")
        roblox_versions.pop(roblox_versions.index(v))

### Downloading and replacing oof sound ###

r = requests.Session().get("https://www.gamespecifications.com/wp-content/uploads/2020/10/roblox-oof-gamespecifications.com_.ogg") # only link i could find :shrug:

print("[OofReverter] Downloaded oof sound effect ")

for v in roblox_versions:
    with open(v+"\content\sounds\ouch.ogg", "wb") as f:
        f.write(r.content)
        print("[OofReverter] Wrote bytes to ogg file: "+ v+"\content\sounds\ouch.ogg")
        f.close()

