#!/bin/bash

find . -name "*~" -delete

for dotfile in `pwd`/home/*; do
	echo Installing `basename $dotfile`
	if [ -d ~/.`basename $dotfile` ]; then
		rm -rf ~/.`basename $dotfile`
	fi
	ln -sf $dotfile ~/.`basename $dotfile`
done

ln -sf `pwd`/other/ycm_extra_conf_default.py ~/.vim/bundle/YouCompleteMe/

sudo cp -rfv etc/ /
