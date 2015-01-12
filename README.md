# DeskPy
This is a  Python script to download Desktop images from http://www.reddit.com/r/wallpapers and automatically set them as your desktop image. These images are saved in a directory next to the script called "Desktops". By default, it searches r/wallpapers for the keyword "space"; however, this could easily be changed to search and subreddit with any keywords.

# Intended Use
This script can be run like any other script; however, it also works nicely being pair with cron. Cron is a scheduler that you can use to automate tasks. Currently, I have this script running every hour with cron. For a tutorial for how to use cron, you can find one <a href=http://www.unixgeeks.org/security/newbie/unix/cron-1.html>here</a>.

# Requirements
As far as I know, this script only works on Linux. It may be updated in the future though.

The only other package neccesary to run this is Praw. Praw is a Reddit API wrapper for python. It can be installed using
<br>
<code>(sudo) pip install praw</code> or found at this <a href=https://github.com/praw-dev/praw>Repo</a>

# Running the Script
<code>python DeskPy.py</code> 
