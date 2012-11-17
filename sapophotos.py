import requests
import json
import urlparse
import dbaccess
import gevent, time

headers = {"Authorization": "ESB AccessKey=5628E260-0518-4DD4-BD50-E98334BFCB32"}
first = True
__SERVICE__ = 'SAPO_PHOTOS'


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
	db = dbaccess.DB()
	searches = db.get_searches_by_service(__SERVICE__)

	check_searches_counter = 0
	while True:
		print('searching...')
		if check_searches_counter % 5 == 0:
			print('getting searches')
			searches = db.get_searches_by_service(__SERVICE__)
		check_searches_counter += 1
		
		print(searches)
		jobs = [gevent.spawn(lambda : do_search(s[0], urllib.unquote(s[1]))) for s in searches]

		gevent.joinall(jobs)

		time_sleep = 300
		print('sleeping for ' + str(time_sleep) + 's...')
		time.sleep(time_sleep)
