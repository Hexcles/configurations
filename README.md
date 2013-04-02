# Hexcles' Configurations

My personal configurations(dotfile and etc).

## home

Mostly some dotfiles under home directory.

## etc

Some global configurations under /etc .

Most of them can be put under home as well(maybe need to rename). I put them in the /etc just because I have several accounts on my laptop and I want to make them the same. If you are on a server or a public workstation, it might be better to use personal configurations instead.

## Font Configuration for Linux

I would like to strongly recommend my font configurations.

The main configuration file is **etc/fonts/local.conf** . You can either put it under /etc/fonts or under your home directory with the name **.fonts.conf** (don't forget the leading dot).

More things you can do: copy the font-relating lines in **etc/xprofile** and **etc/Xresources** to the corresponding files under /etc . They are some tweaks for problematic programs.
