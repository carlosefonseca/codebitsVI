import requests
import json
import urlparse

headers = {"Authorization": "ESB AccessKey=5628E260-0518-4DD4-BD50-E98334BFCB32"}
first = true


def sapophotos(first):
	params = {	tag:"codebits2012",
	r = requests.get('https://services.sapo.pt/Photos/ImageGetListByTags?tag=codebits2012&json=true&ESBUserName=cefonseca@sapo.pt&ESBPassword=saposapo', headers=headers)
	return json.loads(r.content)

def transformImageObject(i):
	img = {}
	for size in i["views"]["view"]:
		if size["size"] == unicode("original"):
			img["media_url"] = size["url"]
			break
	img["descr"] = i["title"]
	img["user"] = i["user"]["username"]
	img["date"] = i["creationDate"]
	img["source"] = i["url"]
	return img


def processSapoImagesArray(response):
	images = response["ImageGetListByTagsResponse"]["ImageGetListByTagsResult"]["images"]["image"]
	imgs = []
	for i in images:
		img = transformImageObject(i)
		imgs.append(img)
	return imgs

x = sapophotos()
l = processSapoImagesArray(x)
print json.dumps(l, indent=2)
print "Size:",len(l)