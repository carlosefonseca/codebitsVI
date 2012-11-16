import flickrapi
import xmlrpclib
from urlparse import urlparse

KEY = "a33101a6bb6c0a7f49146d45183c83b5"
SECRET = "4645d7a5d51ccf75"
flickr = flickrapi.FlickrAPI(KEY)

def figureTheURL(pathstr):
    path = pathstr.strip("/").split("/")
    print "path",path,
    
    if len(path) > 2 and path[0] == "photos":
        user = path[1]
        photoid = path[2]

        photos = flickr.photos_getInfo(photo_id=photoid)
        title = photos.find("photo").find("title").text
        print photos, title
        return photos


    # if path[0]


    # if len(path) == 1:            
    #     if path[0] == "":
    #         print "Homepage. Not allowed."
    #     if path[0] == "photos":
    #         print "Explore. Not allowed."
    #     else:
    #         print "Unknown. Not allowed."
    # 
    # 
    # if len(path) == 0 or len(path) == None:
    #     print "bah"
    # else:
    #     print "humm"


def processURL(url):
    u = urlparse(url)
    allowed = ["flickr.com", "www.flickr.com"]

    print url
    print u.netloc,
    if u.netloc in allowed:
        print "ok"

    return figureTheURL(u.path)
    print

# 
# 
# print pathparts
# 
# if (pathparts[0] == "photos"):
#     user = pathparts[1]
#     photo = pathparts[2]
#     
#     print user," - ",photo
# 
# 
processURL(u"http://flickr.com")
processURL(u"http://flickr.com/photos")
processURL(u"http://flickr.com/photos/whatever-/6893874613/")


photos = []


def processPhotoFromResponse(photo):
    img["media_url"] = "http://farm"+photo.get("farm")+".staticflickr.com/"+photo.get("server")+"/"+photo.get("id")+"_"+photo.get("secret")+"_b.jpg"
    img["descr"] = photo.find("title").text
    img["user"] = photo.find("owner").get("realname")
    img["date"] = photo.find("dates").get("taken")
    img["source"] = photo.find("urls/url[@type='photopage']").text

    return rsp
