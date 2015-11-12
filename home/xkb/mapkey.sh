#!/bin/sh

setxkbmap

if xinput | grep "QuickFire" > /dev/null; then
  exit
fi

xkbcomp -I$HOME/.xkb ~/.xkb/thinkpad_x1 $DISPLAY 2>/dev/null
