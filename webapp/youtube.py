# B.E.A.S.T
# Paragon Orlando 
# Apex
# I'm Not Yelling!
# MVG Sandstorm
# DrommeLAN
# Press Start
# Battle Arena Melbourne
# Get On My Level 
# Smash 'N' Splash
# CEO 
# FC Smash
# WTFox
# EVO 
# Super Smash Con
# Heir II the Throne
# PAX Prime 
# Paragon Los Angeles 
# HTC Throwdown
# DreamHack London 
# Helix
# The Big House
# MLG World Finals 
# DreamHack Winter
import urllib
import json as simplejson
import gdata.youtube
import gdata.youtube.service

# yt_service = gdata.youtube.service.YouTubeService()
# yt_service.developer_key = 'AI39si5C6sxJaFaEyrsUKmOrpPVDqo_fPgTO92BHSGqMgIhw3LItYpvw4BGaMYdQheLJC-B0_ovqmRa4pttdFx-nwC14aInLCQ'
# yt_service.client_id = 'geometric-sled-108103'

GET https://www.googleapis.com/youtube/v3/videos

# https://www.youtube.com/watch?v=WSinMOs5eGw
# id = 'WSinMOs5eGw'
# url = 'https://gdata.youtube.com/feeds/api/videos/#WSinMOs5eGw?alt=json'
#
# print urllib.urlopen(url)
# json = simplejson.load(urllib.urlopen(url))
#
# title = json['entry']['title']['$t']
# author = json['entry']['author'][0]['name']
#
# print "id:%s\nauthor:%s\ntitle:%s" % (id, author, title)


#
# class VideoParser(object):
#     def __init__(self, id, url):
#         self.url = url
#
#     def get_title(self):
#
#          json = simplejson.load(urllib.urlopen(self.url))
#          title = json['entry']['title']['$t']
#
#          print "title:%s" %(title)
#
#     def get_players(self):
#         """
#         Returns a tuple of ints (winner, loser)
#         :return:
#         """
#
#
#         pass
#
#     def get_tournament(self):
#         """
#         Returns a string that is the tournament name
#         :return:
#         """
#         pass
#
# id = "LsKFsF2zpFM"
# url = "https://www.youtube.com/watch?v=LsKFsF2zpFM" % id
#
# vp = VideoParser(id, url)
# print 'title', vp.get_title()
# print 'players', vp.get_players()
# print 'tourney', vp.get_tournament()