from libqtile.config import Group, Match
from consts import *

groups = [
        Group(" 󰣇 "),
        Group("  "),
        Group(" 󰈙 ", matches=[Match(wm_class=[browser])]),
        Group("  "),
        Group(" 󰝚 ", matches=[Match(wm_class=["discord", "spotify-launcher"])]),
]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")
