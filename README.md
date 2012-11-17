The One GalleryA Photo gallery to show photos from multiple sources.Dependencies:	gevent (pip install gevent)		libevent (http://libevent.org/)		cython (pip install cython)*gallery\_service.py*: service offering operations for managing albums and photos## albumGet an album, specified by Id, and all of its photos.#### Parameters:*id*: id of the album to get#### Returns:_JSON_ object containing the name of the album and its list of photos#### Example:*request:*	http://localhost:8088/album?id=123*response:*<pre>	{		"photos": [			{				"user_profile_url": "http://user.com/1", 				"description": "this is a photo", 				"title": "a title", 				"url": "http://a.com/pics/1.jpg", 				"source_url": "http://a.com/source/pic1", 				"thumb_url": "http://a.com/thumbs/thumb_1.jpg", 				"user_name": "user1"			}, 			{				"user_profile_url": "http://user.com/2", 				"description": "this is a photo", 				"title": "a title", 				"url": "http://a.com/pics/2.jpg", 				"source_url": "http://a.com/source/pic2", 				"thumb_url": "http://a.com/thumbs/thumb_2.jpg", 				"user_name": "user2"			}, 			{				"user_profile_url": "http://user.com/3", 				"description": "this is a photo", 				"title": "a title", 				"url": "http://a.com/pics/3.jpg", 				"source_url": "http://a.com/source/pic3", 				"thumb_url": "http://a.com/thumbs/thumb_3.jpg", 				"user_name": "user3"			}, 			{				"user_profile_url": "http://user.com/4", 				"description": "this is a photo", 				"title": "a title", 				"url": "http://a.com/pics/4.jpg", 				"source_url": "http://a.com/source/pic4", 				"thumb_url": "http://a.com/thumbs/thumb_4.jpg", 				"user_name": "user4"			}		], 		"name": "test album"	}	</pre>