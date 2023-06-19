from libqtile import bar, widget 
from libqtile.config import Screen

widget_defaults = dict(
    font="jetbrains mono nerd font",
    fontsize=16,
    padding=3,
)


extension_defaults = widget_defaults.copy()
global_pad = 10
# separator settings, act as global config for bar separators

def init_sep():
    return widget.Sep(
                size_percent=50,
                padding=global_pad
            )

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                #widget.Chord(
                    #chords_colors={
                        #"launch": ("#ff0000", "#ffffff"),
                    #},
                    #name_transform=lambda name: name.upper(),
                #),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                init_sep(),

                widget.CheckUpdates(
                    distro="Arch",
                    no_update_string="0 updates",
                    fmt="󰮯  {}",
                    padding=global_pad,
                    ),

                init_sep(),

                widget.Battery(
                    battery=0,
                    charge_char="",
                    discharge_char="󰉃",
                    full_char=" ",
                    empty_char=" ",
                    format='{char} {percent:2.0%}',
                    padding=global_pad
                    ),

                init_sep(), 

                widget.Volume(
                    fmt=" : {}",
                    emoji=False,
                    padding=global_pad,
                    scroll=True
                    ),

                init_sep(),
                
                #time
                widget.Clock(
                    format=" %I:%M %p",
                    padding=global_pad
                    ),
                
                init_sep(),
                #date
                widget.Clock(
                    format=" %Y-%m-%d %a",
                    padding=global_pad
                    ),

                init_sep(),

                widget.Systray(),
            ],
            40,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
