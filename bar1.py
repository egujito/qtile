from libqtile import bar, widget 
from libqtile.config import Screen
from colors import *

widget_defaults = dict(
    font="jetbrains mono nerd font",
    fontsize=16,
    padding=3,
)


extension_defaults = widget_defaults.copy()
global_pad = 10

# separator settings, act as global config for bar separators
# not using text box for now to make bar more pretty

def init_sep():
    return widget.Spacer(
            length=10
            )

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.GroupBox(
                    disable_drag=True,
                    fontsize=20,
                    ),

                widget.Prompt(),

                widget.WindowName(
                    format="{name}",
                    ),
                #widget.Chord(
                    #chords_colors={
                        #"launch": ("#ff0000", "#ffffff"),
                    #},
                    #name_transform=lambda name: name.upper(),
                #),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                #init_sep(),

                widget.TextBox(
                    fmt="",
                    foreground=colors[red],
                    background="#1D2021",
                    padding=0,
                    fontsize=75
                    ),

                widget.CheckUpdates(
                    distro="Arch",
                    no_update_string="0 updates",
                    fmt="󰮯 {}",
                    padding=global_pad,
                    background=colors[red]
                    ),

                #init_sep(),

                widget.Battery(
                    battery=0,
                    #charge_char="",
                    #discharge_char="󰉃",
                    #full_char=" ",
                    #empty_char=" ",
                    format='  {percent:2.0%}',
                    padding=global_pad,
                    background=colors[orange]
                    ),

                #init_sep(), 

                widget.Volume(
                    fmt=" : {}",
                    emoji=False,
                    padding=global_pad,
                    scroll=True,
                    background=colors[yellow]
                    ),

                
                #time
                widget.Clock(
                    format=" %I:%M %p",
                    padding=global_pad,
                    background=colors[green]
                    ),
                
                #init_sep(),
                #date
                widget.Clock(
                    format=" %Y-%m-%d %a",
                    padding=global_pad,
                    background=colors[aqua]
                    ),

                #init_sep(),

                widget.Systray(
                    background=colors[blue],
                    padding=global_pad,
                    icon_size=50
                    ),

                #init_sep(),

                widget.QuickExit(
                    background=colors[purple],
                    default_text=" ⏻ ",
                    padding=global_pad,
                    countdown_format=" {} "
                    ),
            ],
            40,
            opacity = 1,
            background = "#1D2021"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
