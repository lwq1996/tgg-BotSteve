#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import time
from tools import deprecated
from decimal import *
import os

storage = {} # Default value
# storage is a persistant value, automagically loaded and saved by the bot.

#def setup(self): 
#    pass

@deprecated
def f_seen(self, origin, match, args): 
  """.seen <nick> - Reports when <nick> was last seen."""
  global storage
  
  if origin.sender == '#talis': return
  try:
    nick = match.group(2).lower()
  except AttributeError:
    self.msg(origin.sender, "No user provided!")
    return 
  
  #misc easter eggs
  if nick.lower() == "kyle":
    return self.msg(origin.sender, "He's about this tall?  Seen Kyle?")
  if nick.lower() == "botsteve":
    return self.msg(origin.sender, "I'm right here, actually.")
  
  if storage.has_key(nick): 
      channel, storedTime = storage[nick]
      t = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(storedTime))
      currentTime = time.strftime('%H:%M:%S UTC', time.gmtime())
      rawTimeDifference_hours = (time.time() - storedTime) / 3600
      formattedTimeDiff = Decimal(str(rawTimeDifference_hours)).quantize(Decimal('1.00'))
      
      #requires python 2.7
      #timeDifference_hr = timeDifference_sec.total_seconds() / 3600
      

      msg = "I last saw %s %s hours ago at %s on %s.  Current time: %s" % (nick, formattedTimeDiff, t, channel, currentTime)
      self.msg(origin.sender, str(origin.nick) + ': ' + msg)
  
  #no record of user
  else: self.msg(origin.sender, "Sorry, I haven't seen %s around." % nick)
f_seen.rule = (['seen', 'lastseen'], r'(\S+)')
f_seen.thread = False

@deprecated
def f_note(self, origin, match, args): 
   def note(self, origin, match, args): 
      global storage
      if origin.sender.startswith('#'): 
         # if origin.sender == '#inamidst': return
         storage[origin.nick.lower()] = (origin.sender, time.time())

      # if not hasattr(self, 'chanspeak'): 
      #    self.chanspeak = {}
      # if (len(args) > 2) and args[2].startswith('#'): 
      #    self.chanspeak[args[2]] = args[0]

   try: note(self, origin, match, args)
   except Exception, e: print e
f_note.rule = r'(.*)'
f_note.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
