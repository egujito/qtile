#!/bin/bash

sh ~/.screenlayout/display.sh
feh --bg-scale ~/Pictures/wallpapers/roma.png
bash ~/gtkr.sh
picom --config ~/.config/picom/picom.conf &
