
# coding: utf-8

# In[ ]:




# In[16]:

import praw
import urllib
import os, sys
from random import randrange
from gi.repository import Gio

try:
    
    r = praw.Reddit(user_agent='DeskPy by u/BearClawWednesda')
    submissions = list(r.search('space', 'wallpapers', 'relevance', None, 'alltime', limit=50))
    
    used_submission = submissions[randrange(0,50)]
    
    
    parent_save_dir = os.getcwd()
    
    try:
        os.chdir(parent_save_dir + '/Desktops/')
    except OSError:
        os.makedirs(parent_save_dir + '/Desktops/')
        os.chdir(parent_save_dir + '/Desktops/')
    
    urllib.urlretrieve(used_submission.url, used_submission.name)
        
        
    settings = Gio.Settings.new("org.gnome.desktop.background")
    
    settings.set_string("picture-uri", 'file://' + os.getcwd()+'/' + used_submission.name)
    
except IOError:
    print('Check internet connection and try again')


# In[10]:




# In[ ]:



