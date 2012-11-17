import sqlite3
import hashlib

class DB:

	def __init__(self):
		self.__connection__ = sqlite3.connect('gallery.db')
		self.__cursor__ = self.__connection__.cursor()

	def close(self):
		self.__connection__.close()

	#Check if something exists (e.g. an album with a given name)
	def exists(self, sentence, args=()):
		self.__cursor__.execute(sentence, args)
		check = self.__cursor__.fetchone()

		return check != None


	def get_album_photos(self, album_id):
		rows = []
		for row in self.__cursor__.execute('''
			select
				a.name
				,p.url
				,p.thumb_url
				,p.source_url
				,p.title
				,p.description
				,p.user_name
				,p.user_profile_url
			from
				album a
			inner join
				search s
				on a.id = s.album_id
				and a.id = ?
			inner join
				search2photo s2p
				on s2p.search_id = s.id
			inner join
				photo p
				on s2p.photo_id = p.id
			order by
				p.create_time
			''', (album_id,)):
			rows.append(row)

		return rows

	def get_albums(self):
		rows = []
		for row in self.__cursor__.execute('''
			select
				id
				,name
			from
				album
			order by
				create_time
		'''):
			rows.append(row)

		return rows
				
	def new_album(self, album_name):
		if self.exists('select id from album where name = ?', (album_name,)):
			raise Exception('Album ' + album_name + ' exists')
		
		self.__cursor__.execute('insert into album(name, create_time) values(?, datetime(\'now\'))', (album_name,))
		self.__connection__.commit()
		self.__cursor__.execute('select id from album where name = ?', (album_name,))
		id_row = self.__cursor__.fetchone()
		return id_row[0]

	def get_available_services(self):
		rows = []
		for row in self.__cursor__.execute('select id from service where active = 1'):
			rows.append(row[0])

		return rows

	def get_available_services_regex(self):
		rows = []
		for row in self.__cursor__.execute('select id, url_regex from service where active = 1'):
			rows.append(row)

		return rows

	def new_search(self, album_id, service_id, url):
		if not self.exists('select id from album where id = ?', (album_id,)):
			raise Exception('Album #' + str(album_id) + ' does not exist')
		if not self.exists('select id from service where id = ? and active = 1', (service_id,)):
			raise Exception('Service ' + str(service_id) + ' does not exist or is not active')
		if self.exists('select id from search where album_id = ? and service_id = ? and search_url = ?', (album_id, service_id, url)):
			raise Exception('Search already exists')

		self.__cursor__.execute('insert into search(album_id, service_id, search_url, create_time) values(?, ?, ?, datetime(\'now\'))', (album_id, service_id, url))
		self.__connection__.commit()

	def new_photo(self, imgid, url, source_url = "", thumb_url = "", title = "", description = "", user_name = "", user_profile_url = "", create_time = ""):
		if not url:
			raise Exception("URL required.")
		
 		self.__cursor__.execute('''insert into photo (id, url, source_url, thumb_url, title, description, user_name, user_profile_url, create_time)
											   values(?, 	?, 			?, 		?, 		?, 			?, 			?, 			?, 			?)''',
											   		imgid, url, source_url, thumb_url, title, description, user_name, user_profile_url, create_time)
		self.__connection__.commit()


	def new_photo_on_search(self, search_id, imgid):
		self.__cursor__.execute('''insert into search2photo (search_id, photo_id) values (?, ?)''', search_id, imgid)
		self.__connection__.commit();

	def new_photo_from_search(self, search_id, url, source_url, thumb_url, title, description, user_name, user_profile_url, create_time):
		imgid = calculateId(url) 		
		new_photo(self, imgid, url, source_url, thumb_url, title, description, user_name, user_profile_url, create_time)
		new_photo_on_search(search_id, imgid)

	def calculateId(url) {
		# devia-se fazer alguma filtragem do URL
		return hashlib.md5(url).hexdigest()
	}
