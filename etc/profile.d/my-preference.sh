# /etc/profile.d/my-preference.conf

# Use Vim!
export EDITOR=vim

# Display messages in English when we're not running desktop.
if [ -z $DESKTOP_SESSION ]; then
	export LC_MESSAGES=en_US.UTF-8
fi
