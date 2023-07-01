## this code is added by the (C) TheTeamAlexa on 7th March
# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki


import random
from AnonX.utils.database import get_theme

themes = [
    "anonx",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
