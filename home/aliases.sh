#!/bin/bash

#alias goagent='(cd ~/bin/goagent && nohup python2 proxy.py 2> /dev/null &)'
alias shadowsocks='nohup ss-local -c ~/bin/shadowsocks.json --fast-open >/dev/null 2>&1 &'
#alias setproxy='export http_proxy="http://127.0.0.1:3128" && export https_proxy="https://127.0.0.1:3128"'

# Colorful commands
alias ls='ls --color=auto'
alias grep='grep --color=auto'

alias ll='ls -l'

# Handy shortcuts
alias open='xdg-open'
alias douban.fm='python2 ~/studio/douban.fm/douban/douban.py'
alias canvas_decode='~/bin/canvas_urldecode.py'
