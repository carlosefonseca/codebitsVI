The One Gallery

A Photo gallery to show photos from multiple sources.

Dependencies:
	gevent (pip install gevent)
		libevent (http://libevent.org/)
		cython (pip install cython)


*gallery\_service.py*: service offering operations for managing albums and photos

## album

Get an album, specified by Id, and all of its photos.

#### Parameters:
*id*: id of the album to get

#### Returns:
_JSON_ object containing the name of the album and its list of photos

#### Example:

*request:*
	http://localhost:8088/album?id=123

*response:*
<pre>
	{
		"photos": [
			{
				"user_profile_url": "http://user.com/1", 
				"description": "this is a photo", 
				"title": "a title", 
				"url": "http://a.com/pics/1.jpg", 
				"source_url": "http://a.com/source/pic1", 
				"thumb_url": "http://a.com/thumbs/thumb_1.jpg", 
				"user_name": "user1"
			}, 
			{
				"user_profile_url": "http://user.com/2", 
				"description": "this is a photo", 
				"title": "a title", 
				"url": "http://a.com/pics/2.jpg", 
				"source_url": "http://a.com/source/pic2", 
				"thumb_url": "http://a.com/thumbs/thumb_2.jpg", 
				"user_name": "user2"
			}, 
			{
				"user_profile_url": "http://user.com/3", 
				"description": "this is a photo", 
				"title": "a title", 
				"url": "http://a.com/pics/3.jpg", 
				"source_url": "http://a.com/source/pic3", 
				"thumb_url": "http://a.com/thumbs/thumb_3.jpg", 
				"user_name": "user3"
			}, 
			{
				"user_profile_url": "http://user.com/4", 
				"description": "this is a photo", 
				"title": "a title", 
				"url": "http://a.com/pics/4.jpg", 
				"source_url": "http://a.com/source/pic4", 
				"thumb_url": "http://a.com/thumbs/thumb_4.jpg", 
				"user_name": "user4"
			}
		], 
		"name": "test album"
	}	
</pre>

## albums

Get the list of existing albums

#### Parameters:
_none_

#### Returns:
_JSON_ object containing the list of existing albums

#### Example:
*request*:
http://localhost:8088/albums

*response:*
<pre>
	[{"id": 123, "name": "test album"}]
</pre>


## add\_album

Allows to create a new album

#### Parameters:
*name*: the album's name

#### Returns:
If album created correctly:
	The new album's Id
If the name already exists:
	_JSON_ object with the reason for the error

#### Example:
*request*:
http://localhost:8088/add_album?name=test

*response:*
<pre>
	(success)
	125

	(error)
	{"error": "Album test exists"}
</pre>

## services

Get the list of the available services

#### Parameters:
_none_

#### Returns:
_JSON_ list of service IDs (strings)

#### Example:
*request*:
http://localhost:8088/services

*response:*
<pre>
	[
		"TWITTER"
	]
</pre>

## add\_search

Allows to add a new search to an album

#### Parameters:
*album_id*: ID of the album to add the search to
*url*: search url

#### Returns:
If search added correctly:
	"OK"
If not:
	_JSON_ object detailing the reason for the error

#### Example:
*request*:
http://localhost:8088/add_search?album_id=126&url=https%3A%2F%2Ftwitter.com%2Fsearch%3Fq%3Dcodebits%26src%3Dtypsds

*response:*
<pre>
	(success)
	"OK"

	(error)
	{"error": "Album #126 does not exist"}
</pre>
