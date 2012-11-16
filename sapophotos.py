import requests
import json
import urlparse

headers = {"Authorization": "ESB AccessKey=5628E260-0518-4DD4-BD50-E98334BFCB32"}

def sapophotos():
	r = requests.get('https://services.sapo.pt/Photos/ImageGetListByTags?tag=codebits2012&json=true&ESBUserName=cefonseca@sapo.pt&ESBPassword=saposapo', headers=headers)
	return json.loads(r.content)


x = sapophotos()
