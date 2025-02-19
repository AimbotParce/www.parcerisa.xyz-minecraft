import json
import os
import pathlib

from mojang import API

SERVER_FOLDER = pathlib.Path(os.environ["SERVER_FOLDER"])

STATS_FOLDER = SERVER_FOLDER / "world" / "stats"


uuid2name = {}


def get_player_playtime_hours():
    api = API()

    players = []
    playtime = []
    for player_file in STATS_FOLDER.iterdir():
        if player_file.is_file():
            player_uuid = player_file.stem
            if not player_uuid in uuid2name:
                uuid2name[player_uuid] = api.get_username(player_uuid)
                if uuid2name[player_uuid] is None:
                    uuid2name[player_uuid] = "UNKNOWN"
            players.append(uuid2name[player_uuid])
            with open(player_file, "r") as f:
                data = json.load(f)
                playtime.append(data["stats"]["minecraft:custom"]["minecraft:play_time"] / 72000)

    return players, playtime
