#!/usr/bin/python
# -*- coding: utf-8 -*-

from twython import Twython
from bs4 import BeautifulSoup
import pprint
import json
import re
import requests

def print_dict(dict):
    """ 
    print dictionary
    """
    for key,value in dict.items():
        print(key,value) 

regex1 = re.compile('http://(?:www\\.)?xkcd\\.com/\\d+/?|http://soundcloud.com/.*/.*|http://(?:www\\.)?flickr\\.com/.*|http://www\\.ted\\.com/talks/[^/]+\\.html|http://.*\\.viddler\\.com/.*|http://yfrog\\.com/[0-9a-zA-Z]+/?$|https?://(?:www.)?skitch.com/([^/]+)/[^/]+/.+|http://skit.ch/[^/]+|https?://gist\\.github\\.com/([0-9a-fA-f]+)|https?://www\\.(dropbox\\.com/s/.+\\.(?:jpg|png|gif))|https?://db\\.tt/[a-zA-Z0-9]+|https?://[^\\.]+\\.wikipedia\\.org/wiki/[^#]+(?:#(.+))?|http://www.traileraddict.com/trailer/[^/]+/trailer|http://lockerz\\.com/[sd]/\\d+|http://trailers\\.apple\\.com/trailers/[^/]+/[^/]+|http://bash\\.org/\\?(\\d+)|http://imgur\\.com/gallery/[0-9a-zA-Z]+|http://www\\.asciiartfarts\\.com/[0-9]+\\.html|https?://(?:[^\\.]+\\.)?youtube\\.com/watch/?\\?(?:.+&)?v=([^&]+)|https?://youtu\\.be/([a-zA-Z0-9_-]+)|https?://github\\.com/([^/]+)/([^/]+)/commit/(.+)|http://git\\.io/[_0-9a-zA-Z]+|https?://open\\.spotify\\.com/(track|album)/([0-9a-zA-Z]{22})|https?://path\\.com/p/([0-9a-zA-Z]+)$|http://www.funnyordie.com/videos/[^/]+/.+|http://(?:www\\.)?twitpic\\.com/([^/]+)|https?://www\\.giantbomb\\.com/[^/]+/\\d+-\\d+/?|http://(?:www\\.)?beeradvocate\\.com/beer/profile/\\d+/\\d+|http://(?:www\\.)?imdb.com/title/(tt\\d+)|http://cl\\.ly/[0-9a-zA-Z]+/?$|http://www\\.hulu\\.com/watch/.*|https?://(?:www\\.)?twitter\\.com/(?:#!/)?[^/]+/status(?:es)?/(\\d+)/?$|http://t\\.co/[a-zA-Z0-9]+|https?://(?:www\\.)?vimeo\\.com/.+|http://www\\.amazon\\.com/(?:.+/)?[gd]p/(?:product/)?(?:tags-on-product/)?([^/]+)|http://amzn\\.com/([^/]+)|http://qik\\.com/video/.*|http://www\\.rdio\\.com/#/artist/[^/]+/album/[^/]+/?|http://www\\.rdio\\.com/#/artist/[^/]+/album/[^/]+/track/[^/]+/?|http://www\\.rdio\\.com/#/people/[^/]+/playlists/\\d+/[^/]+|http://www\\.slideshare\\.net/.*/.*|http://imgur\\.com/([0-9a-zA-Z]+)$|https?://www\\.facebook\\.com/([^/]+)/posts/(\\d+)|https?://instagr(?:\\.am|am\\.com)/p/.+|http://www\\.twitlonger\\.com/show/[a-zA-Z0-9]+|http://tl\\.gd/[^/]+|http://www\\.urbandictionary\\.com/define\\.php\\?term=.+|http://picplz\\.com/user/[^/]+/pic/[^/]+|https?://pic\\.twitter\\.com/.+|https?://(?:www\\.)?twitter\\.com/(?:#!/)?[^/]+/status(?:es)?/(\\d+)/photo/\\d+/?$')


def validURL(url):
    return regex1.match(url);



'''
oauth_token and oauth_token_secret come from the previous step
if needed, store those in a session variable or something
'''

t = Twython(app_key="yMNdpqYz5ke32Z6jCZsE7w",
            app_secret="5oDqxINNVOH1CHDJdUp2Mz3nwEgbBGeczJufD957S2k",
            oauth_token="15439239-rJspSTXhfu4hnJ7MyT4iJUagmsg8I3HV9zsTTPs",
            oauth_token_secret="nUeFkU3HVOXsVUFNJPljGbDvqF0apKimHvXFQ3dvNA")

raw = t.get(endpoint="https://api.twitter.com/1.1/search/tweets.json", params={'q':"codebits -won -badge filter:links", 'count':100, 'result_type':'recent'})

#pprint.PrettyPrinter(indent=4).pprint(raw)

imgs = []

for x in raw.get(unicode("statuses")):
    y = x.get(unicode("entities"))
    y = y.get(unicode("urls"))
    for urlobj in y:
        url = urlobj.get(unicode("expanded_url"))
        if validURL(url):
            r = requests.get('http://noembed.com/embed', params={'url': url})
            img = {}
            img["media_url"] = unicode(json.loads(r.content).get("media_url"))
            img["descr"] = x.get(unicode("text"))
            img["user"] = x.get(unicode("user")).get(unicode("name"))
            img["date"] = x.get(unicode("created_at"))
            img["source"] = url
            imgs.append(img)
            


pprint.PrettyPrinter(indent=2).pprint(imgs)