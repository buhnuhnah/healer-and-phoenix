init python:
    def save_extra_data(d):
         d["playtime"] = renpy.get_game_runtime()
         d["chapter"] = chapter_no
         d["name"] = player_name
    config.save_json_callbacks = [save_extra_data]

    config.searchpath.extend(["game/audio", "game/images/backgrounds"])
    centerTextbox = False
