from libqtile import bar, widget 
from libqtile.config import Screen

widget_defaults = dict(
    font="jetbrains mono nerd font",
    fontsize=16,
    padding=3,
)


extension_defaults = widget_defaults.copy()

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
                widget.Systray(),
                widget.Clock(format=" %I:%M %p |  %Y-%m-%d %a"),
            ],
            40,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
