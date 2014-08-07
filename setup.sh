#!/bin/bash

ln -sf `pwd`/home/profile ~/.profile
ln -sf `pwd`/home/vimrc ~/.vimrc
ln -sf `pwd`/home/gvimrc ~/.gvimrc
ln -sf `pwd`/home/ycm_extra_conf_default.py ~/.vim/bundle/YouCompleteMe/

sudo cp -rf etc/ /etc/
