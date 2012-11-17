#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
import json
import re
import requests
from dbaccess import DB

class GenericGrabber():

    regex1 = re.compile('http://(?:www\\.)?xkcd\\.com/\\d+/?|http://(?:www\\.)?flickr\\.com/.*|http://yfrog\\.com/[0-9a-zA-Z]+/?$|https?://(?:www.)?skitch.com/([^/]+)/[^/]+/.+|http://skit.ch/[^/]+|https?://www\\.(dropbox\\.com/s/.+\\.(?:jpg|png|gif))|https?://db\\.tt/[a-zA-Z0-9]+|http://lockerz\\.com/[sd]/\\d+|http://imgur\\.com/gallery/[0-9a-zA-Z]+|http://www\\.asciiartfarts\\.com/[0-9]+\\.html|https?://(?:[^\\.]+\\.)?youtube\\.com/watch/?\\?(?:.+&)?v=([^&]+)|https?://youtu\\.be/([a-zA-Z0-9_-]+)|https?://github\\.com/([^/]+)/([^/]+)/commit/(.+)|http://git\\.io/[_0-9a-zA-Z]+|https?://open\\.spotify\\.com/(track|album)/([0-9a-zA-Z]{22})|https?://path\\.com/p/([0-9a-zA-Z]+)$|http://www.funnyordie.com/videos/[^/]+/.+|http://(?:www\\.)?twitpic\\.com/([^/]+)|https?://www\\.giantbomb\\.com/[^/]+/\\d+-\\d+/?|http://(?:www\\.)?beeradvocate\\.com/beer/profile/\\d+/\\d+|http://(?:www\\.)?imdb.com/title/(tt\\d+)|http://cl\\.ly/[0-9a-zA-Z]+/?$|http://www\\.hulu\\.com/watch/.*|https?://(?:www\\.)?twitter\\.com/(?:#!/)?[^/]+/status(?:es)?/(\\d+)/?$|http://t\\.co/[a-zA-Z0-9]+|https?://(?:www\\.)?vimeo\\.com/.+|http://www\\.amazon\\.com/(?:.+/)?[gd]p/(?:product/)?(?:tags-on-product/)?([^/]+)|http://amzn\\.com/([^/]+)|http://qik\\.com/video/.*|http://www\\.rdio\\.com/#/artist/[^/]+/album/[^/]+/?|http://www\\.rdio\\.com/#/artist/[^/]+/album/[^/]+/track/[^/]+/?|http://www\\.rdio\\.com/#/people/[^/]+/playlists/\\d+/[^/]+|http://www\\.slideshare\\.net/.*/.*|http://imgur\\.com/([0-9a-zA-Z]+)$|https?://www\\.facebook\\.com/([^/]+)/posts/(\\d+)|https?://instagr(?:\\.am|am\\.com)/p/.+|http://www\\.twitlonger\\.com/show/[a-zA-Z0-9]+|http://tl\\.gd/[^/]+|http://www\\.urbandictionary\\.com/define\\.php\\?term=.+|http://picplz\\.com/user/[^/]+/pic/[^/]+|https?://pic\\.twitter\\.com/.+|https?://(?:www\\.)?twitter\\.com/(?:#!/)?[^/]+/status(?:es)?/(\\d+)/photo/\\d+/?$')

    db = DB()

    def validURL(self, url):
        return self.regex1.match(url);

    def getImageDetails(self, url):
        r = requests.get('http://noembed.com/embed', params={'url': url})
        rj = json.loads(r.content)
        if rj.get("type") == "photo":
            img = {}
            img["url"] = unicode(rj.get("media_url"))
            img["title"] = unicode(rj.get("title"))
            img["source_url"] = url
            return img
                
#   def new_photo_from_search(self, search_id, url, source_url, thumb_url, title, description, user_name, user_profile_url, create_time):

    def do_search(self, search_id, url):
        if self.validURL(url):
            x = self.getImageDetails(url)
            if x:
                self.savePhoto(search_id, x)

    def savePhoto(self, search_id, x):
        self.db.new_photo_from_search(search_id, url = x["url"], source_url = x["source_url"], title = x["title"])



if __name__ == "__main__":
    g = GenericGrabber()
    g.do_search(999, "http://instagr.am/p/SDo-9ILbwJ")