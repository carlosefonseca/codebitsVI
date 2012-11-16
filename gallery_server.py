#!/usr/bin/python
"""WSGI server example"""
from gevent.pywsgi import WSGIServer
import urlparse, json, dbaccess


def application(env, start_response):
	operation = env['PATH_INFO']

	if operation == '/album':
		qs = urlparse.parse_qs(env['QUERY_STRING'])
		if 'id' in qs:
			db = dbaccess.DB()

			album_id = qs['id'][0]
			callback = qs['callback'][0]

			photos = db.get_album_photos(album_id)
			response = {'name': '', 'photos':[]}

			if len(photos) > 0:
				response['name'] = photos[0][0]
				response['photos'] = [{
					'url': p[1]
					,'thumb_url': p[2]
					,'source_url': p[3]
					,'title': p[4]
					,'description': p[5]
					,'user_name': p[6]
					,'user_profile_url': p[7]
				} for p in photos]

			start_response('200 OK', [('Content-Type', 'application/json')])

			db.close()
			return [callback + '(' + json.dumps(response) + ')']

	if operation == '/albums':
		db = dbaccess.DB()
		albums = db.get_albums()

		db.close()
		start_response('200 OK', [('Content-Type', 'application/json')])
		return [callback + '(' + json.dumps([{'id': a[0], 'name': a[1]} for a in albums]) + ')']

	#If everything else fails...
	start_response('404 Not Found', [('Content-Type', 'text/html')])
	return ['<h1>Not Found</h1>']


if __name__ == '__main__':
    print 'Serving on 8088...'
    WSGIServer(('', 8088), application).serve_forever()

