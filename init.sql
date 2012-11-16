drop table if exists search2photo;
drop table if exists search;
drop table if exists service;
drop table if exists album;
drop table if exists photo;

create table photo(
	id text primary key -- URL hash
	,url text not null
	,source_url text null
	,thumb_url text null
	,title text null
	,description text null
	,user_name text null
	,user_profile_url text null
	,create_time integer not null
);

create table album(
	id integer primary key
	,name text not null
	,create_time integer not null
);

create table service(
	id text primary key
	,handler_url text not null
	,url_regex text not null
	,active integer not null default 1
	,create_time integer not null
);

create table search(
	id integer primary key
	,service_id text not null
	,album_id integer not null
	,search_url text not null
	,create_time integer not null
);

create table search2photo(
	id integer primary key
	,search_id integer not null
	,photo_id text not null
	,create_time integer not null
);

