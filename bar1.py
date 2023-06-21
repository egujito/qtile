from libqtile import bar, widget 
from libqtile.config import Screen
from qtile_extras import widget as extra
from qtile_extras.widget.decorations import BorderDecoration

from gruvbox import *

from consts import *

widget_defaults = dict(
    font="jetbrains mono nerd font",
    fontsize=16,
    padding=3,
)


extension_defaults = widget_defaults.copy()
global_pad = 5

# separator settings, act as global config for bar separators
# not using text box for now to make bar more pretty

def init_sep():
    return widget.Sep(

            )

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.GroupBox(
                    disable_drag=True,
                    fontsize=20,
                    highlight_method='line',
                    highlight_color='#1D2021',
                    active=colors[green],
                    block_highlight_text_color=colors[purple],
                    this_current_screen_border=colors[purple],
                    ),

                init_sep(),

                extra.CurrentLayoutIcon(
                    scale=0.7,
                    use_mask=True,
                    foreground=colors[purple],
                    ),

                widget.Prompt(
                    foreground=colors[green],
                    ),
                
                init_sep(),

                widget.WindowName(
                    format="{name}",
                    fontsize=14,
                    foreground=colors[purple],
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

                # POWERLINE-LIKE ENDING TO THE BAR
                #widget.TextBox(
                    #fmt="",
                    #foreground=colors[red],
                    #background="#1D2021",
                    #padding=0,
                    #fontsize=75
                    #),
                
                #widget.CPUGraph(
                    #type="line",
                    #border_width=0,
                    #line_width=1,
                    #graph_color=colors[blue],
                    #frequency=0.1,
                    #samples=100
                    #),

                widget.Memory(
                    foreground=colors[blue],
                    measure_mem='G',
                    fmt="󰍛 {}",
                    decorations=[
                        BorderDecoration(
                            colour = colors[blue],
                            border_width= [0, 0, 4, 0],
                            padding_x = 5
                        ),
                    ]
                ), 

                widget.DF(
                    visible_on_warn=False,
                    foreground=colors[purple],
                    format="{f}{m}/{s}{m}",
                    padding=global_pad,
                    fmt="󰑹 {}",
                    decorations=[
                        BorderDecoration(
                            colour = colors[purple],
                            border_width= [0, 0, 4, 0],
                            padding_x = 5
                            ),

                        ]
                    ),

                widget.CheckUpdates(
                    foreground = colors[red],
                    colour_have_updates = colors[red],
                    colour_no_updates = colors[red],
                    distro=updt_cmd,
                    fmt="󰮯 {}",
                    initial_text="Loading updates...",
                    padding=global_pad,
                    decorations=[
                        BorderDecoration(
                            colour = colors[red],
                            border_width= [0, 0, 4, 0],
                            padding_x = 5
                            ),

                        ]
                    ),

                #init_sep(),

                
                #widget.UPowerWidget(),
                #widget.Battery(
                    #foreground=colors[orange],
                    #battery=0,
                    #charge_char="",
                    #discharge_char="󰉃",
                    #full_char=" ",
                    #empty_char=" ",
                    #format='{char} {percent:2.0%}',
                    #padding=global_pad,
                    #decorations=[
                        #BorderDecoration(
                            #colour = colors[orange],
                            #border_width= [0, 0, 4, 0],
                            #padding_x = 5
                            #),

                        #]
                    #),


                extra.UPowerWidget(
                    border_charge_colour=colors[orange],
                    border_colour=colors[orange],
                    border_critical_colour=colors[red],
                    fill_charge=colors[orange],
                    fill_critical=colors[red],
                    fill_low=colors[orange],
                    fill_normal=colors[orange],
                    foreground=colors[orange],
                    text_charging="󰉁 {percentage:.0f}%",
                    text_discharging="󰉃 {percentage:.0f}%",
                    decorations= [
                        BorderDecoration(
                            colour = colors[orange],
                            border_width= [0, 0, 4, 0],
                            padding_x = 2
                            ),
                        ]
                    ),

                #init_sep(), 

                widget.Volume(
                    foreground=colors[yellow],
                    fmt=" : {}",
                    emoji=False,
                    padding=global_pad,
                    scroll=True,
                    decorations=[
                        BorderDecoration(
                            colour = colors[yellow],
                            border_width= [0, 0, 4, 0],
                            padding_x = 5
                            ),

                        ]
                    ),

                
                #time
                widget.Clock(
                    foreground=colors[green],
                    format=" %I:%M %p",
                    padding=global_pad,
                    decorations=[
                        BorderDecoration(
                            colour = colors[green],
                            border_width= [0, 0, 4, 0],
                            padding_x = 5
                            ),

                        ]

                    ),
                
                #init_sep(),
                #date
                widget.Clock(
                    foreground=colors[aqua],
                    format=" %Y-%m-%d %a",
                    padding=global_pad,
                    decorations=[
                        BorderDecoration(
                            colour = colors[aqua],
                            border_width= [0, 0, 4, 0],
                            padding_x = 5
                            ),

                        ]
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
