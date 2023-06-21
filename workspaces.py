from libqtile.config import Group, Match
from consts import *

groups = [
        Group("dev"),
        Group("sys"),
        Group("www", matches=[Match(wm_class=[browser])]),
        Group("game"),
        Group("chat", matches=[Match(wm_class=["discord", "Spotify"])]),
]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")
