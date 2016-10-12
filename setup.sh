#!/bin/bash

# get rid of backup files
find . -name "*~" -delete

# home dotfiles
for dotfile in `pwd`/home/*; do
	echo Installing `basename $dotfile`
	if [ -d ~/.`basename $dotfile` ]; then
		rm -rf ~/.`basename $dotfile`
	fi
	ln -sf $dotfile ~/.`basename $dotfile`
done

# etc
sudo cp -rfv etc/ /

# extra
ln -sf `pwd`/other/ycm_extra_conf_default.py ~/.vim/bundle/YouCompleteMe/
sudo cp other/xkb/* /usr/share/X11/xkb/symbols/
if ! grep -q us-x1 /usr/share/X11/xkb/rules/evdev.xml; then
	sudo patch /usr/share/X11/xkb/rules/evdev.xml other/xkb/evdev.xml.patch
fi

# dconf
echo "Loading dconf dump"
dconf load /org/gnome/terminal/legacy/profiles:/ < `pwd`/dconf/terminal_profile
