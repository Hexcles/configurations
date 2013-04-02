#!/bin/bash

ln -sf ./home/vimrc ~/.vimrc
ln -sf ./home/gvimrc ~/.gvimrc

sudo cp -f ./etc/xprofile /etc/xprofile
sudo cp -f ./etc/Xresources /etc/Xresources
sudo cp -f ./etc/fonts.conf /etc/fonts/fonts.conf
sudo cp -f ./etc/vimrc /etc/vimrc
