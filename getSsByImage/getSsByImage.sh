#!/bin/sh

if [ -e $HOME/temp.png ]; then
    rm $HOME/temp.png
    rm $HOME/crop_tes*
fi

# screen shot in 3s
gnome-screenshot -d 5 -f $HOME/temp.png

sleep 1

python3 imageToJson.py 
