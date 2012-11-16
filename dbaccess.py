import sqlite3

class DB:

	def __init__(self):
		self.__connection__ = sqlite3.connect('gallery.db')
		self.__cursor__ = self.__connection__.cursor()

	def close(self):
		self.__connection__.close()

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
				
