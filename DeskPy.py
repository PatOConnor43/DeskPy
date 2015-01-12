import praw
import urllib
import os, sys
from random import randrange


try:
    
    r = praw.Reddit(user_agent='DeskPy by u/BearClawWednesda')
    submissions = list(r.search('space', 'wallpapers', 'relevance', None, 'alltime', limit=50))
    
    used_submission = submissions[randrange(0,50)]
    
    
    parent_save_dir = os.path.abspath(os.path.dirname(__file__))
    
    try:
        os.chdir(parent_save_dir + '/Desktops/')
    except OSError:
        os.makedirs(parent_save_dir + '/Desktops/')
        os.chdir(parent_save_dir + '/Desktops/')
    
    urllib.urlretrieve(used_submission.url, used_submission.name)
        
    
    setup = 'file://' + os.getcwd() + '/' + used_submission.name
    os.system("DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri '%s'" % (setup))
    
    
except IOError:
    print('Check internet connection and try again')



