import requests
import json
import urlparse
from dbaccess import DB

headers = {"Authorization": "ESB AccessKey=5628E260-0518-4DD4-BD50-E98334BFCB32"}
first = True
db = DB()


def sapophotos(first):
    r = requests.get('https://services.sapo.pt/Photos/ImageGetListByTags?tag=codebits2012&json=true&ESBUserName=cefonseca@sapo.pt&ESBPassword=saposapo', headers=headers)
    return json.loads(r.content)

def transformImageObject(i):
    img = {}
    for size in i["views"]["view"]:
        if size["size"] == unicode("original"):
            img["url"] = size["url"]
        elif size["size"] == unicode("normal"):
            img["thumb_url"] = size["url"]
    img["title"] = i["title"]
    img["user"] = i["user"]["username"]
    img["date"] = i["creationDate"]
    img["source_url"] = i["url"]
    return img

def do_search(search_id, url):
    x = sapophotos(True)
    l = processSapoImagesArray(x)

    for i in l:
        savePhoto(search_id, i)

def processSapoImagesArray(response):
    images = response["ImageGetListByTagsResponse"]["ImageGetListByTagsResult"]["images"]["image"]
    imgs = []
    for i in images:
        img = transformImageObject(i)
        imgs.append(img)
    return imgs

def savePhoto(search_id, x):
    db.new_photo_from_search(search_id, url = x["url"], source_url = x["source_url"], title = x["title"], thumb_url = x["thumb_url"], user_name = x["user"], create_time = x["date"])


if __name__ == "__main__":
    do_search(20, "")