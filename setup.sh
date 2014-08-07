#!/bin/bash

find . -name "*~" -delete

for dotfile in `pwd`/home/*; do
	ln -sf $dotfile ~/.`basename $dotfile`
done
ln -sf `pwd`/other/ycm_extra_conf_default.py ~/.vim/bundle/YouCompleteMe/

sudo cp -rf etc/ /etc/
