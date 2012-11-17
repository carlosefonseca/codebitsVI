#!/usr/bin/python
"""WSGI server example"""
from gevent.pywsgi import WSGIServer
import urlparse, json, dbaccess, re, urllib, gevent
import dummy_grabber, flickr, twitter, generic #, sapophotos


__GRABBERS__ = {
		'TWITTER': twitter,
		'FLICKR': flickr,
		#'SAPO_PHOTOS': sapophotos,
		'DUMMY': dummy_grabber,
		'GENERIC': generic.GenericGrabber()
}

def application(env, start_response):

	#handle the possibility of a jsonp callback
	def do_return(json, qs, code='200 OK'):
		start_response(code, [('Content-Type', 'application/json')])
		if "callback" in qs:
			callback = qs['callback'][0]
			return [callback + '(' + json + ')']
		return json


	operation = env['PATH_INFO']

	if operation == '/album': ############################################### album
		qs = urlparse.parse_qs(env['QUERY_STRING'])
		if 'id' in qs:
			db = dbaccess.DB()

			album_id = qs['id'][0]

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

			db.close()
			jsresp = json.dumps(response, indent=2)
			return do_return(jsresp, qs)


	if operation == '/albums': ############################################### albums
		db = dbaccess.DB()
		albums = db.get_albums()

		qs = urlparse.parse_qs(env['QUERY_STRING'])

		db.close()
		jsresp = json.dumps([{'id': a[0], 'name': a[1]} for a in albums])

		return do_return(jsresp, qs)

	if operation == '/add_album': ############################################### add_album
		qs = urlparse.parse_qs(env['QUERY_STRING'])

		if 'name' in qs:
			try:
				album_name = qs['name'][0]

				db = dbaccess.DB()
				id = db.new_album(album_name)

				db.close()

				return do_return(json.dumps(id), qs)
			except Exception as e:
				return do_return(json.dumps({'error': str(e)}), qs, '500 Internal Server Error')


	if operation == '/services': ############################################### services
		qs = urlparse.parse_qs(env['QUERY_STRING'])

		db = dbaccess.DB()
		services = db.get_available_services()

		db.close()

		return do_return(json.dumps(services, indent=2), qs)

	if operation == '/add_search': ############################################### add_search
		qs = urlparse.parse_qs(env['QUERY_STRING'])
		if 'url' in qs and 'album_id' in qs:
			url = qs['url'][0]
			album_id = qs['album_id'][0]

			db = dbaccess.DB()
			services = db.get_available_services_regex()

			service_id = None
			for s in services:
				if re.match(s[1], url):
					service_id = s[0]

			if service_id is None:
				service_id = __GRABBERS__["GENERIC"]
				# return do_return(json.dumps({'error': 'The search url does not specify any active service'}), qs, '500 Internal Server Error')

			# try:
				#save the new search and call the respective grabber
			id = db.new_search(album_id, service_id, urllib.quote(url))
			gevent.spawn(lambda : __GRABBERS__[service_id].do_search(id, url))
			# except Exception as e:
				# return do_return(json.dumps({'error': str(e)}), qs, '500 Internal Server Error')

			return do_return(json.dumps('OK'), qs)


	#If everything else fails...
	start_response('404 Not Found', [('Content-Type', 'text/html')])
	return ['<h1>Not Found</h1>']


if __name__ == '__main__':
    print 'Serving on 8088...'
    WSGIServer(('', 8088), application).serve_forever()

