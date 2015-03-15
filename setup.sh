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

# extra
ln -sf `pwd`/other/ycm_extra_conf_default.py ~/.vim/bundle/YouCompleteMe/

# etc
sudo cp -rfv etc/ /

# dconf
echo "Loading dconf dump"
dconf load /org/gnome/terminal/legacy/profiles:/ < `pwd`/dconf/terminal_profile
