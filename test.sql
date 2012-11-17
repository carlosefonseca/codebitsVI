insert into service(id, handler_url, url_regex, active, create_time)
values ('TWITTER', '', 'https?://twitter.com/search?.*q=([^&]+).*', 1, datetime('now')),
('FLICKR', '', 'https?://www.flickr.com/search/?.*q=([^&]+).*', 1, datetime('now')),
('SAPO_PHOTOS', '', 'http://fotos.sapo.pt/pesquisa?.*termos=([^&]+).*', 1, datetime('now'));

insert into album(rowid, name, create_time)
values (123, 'test album', datetime('now'));

insert into search(rowid, service_id, album_id, search_url, create_time)
values (1, 'TWITTER', 123, 'a', datetime('now')),
(2, 'TWITTER', 123, 'b', datetime('now'));

insert into photo(id, url, source_url, thumb_url, title, description, user_name, user_profile_url, create_time)
values ('12345', 'http://a.com/pics/1.jpg', 'http://a.com/source/pic1', 'http://a.com/thumbs/thumb_1.jpg', 'a title', 'this is a photo', 'user1', 'http://user.com/1', datetime('now')),
('22345', 'http://a.com/pics/2.jpg', 'http://a.com/source/pic2', 'http://a.com/thumbs/thumb_2.jpg', 'a title', 'this is a photo', 'user2', 'http://user.com/2', datetime('now')),
('32345', 'http://a.com/pics/3.jpg', 'http://a.com/source/pic3', 'http://a.com/thumbs/thumb_3.jpg', 'a title', 'this is a photo', 'user3', 'http://user.com/3', datetime('now')),
('42345', 'http://a.com/pics/4.jpg', 'http://a.com/source/pic4', 'http://a.com/thumbs/thumb_4.jpg', 'a title', 'this is a photo', 'user4', 'http://user.com/4', datetime('now'));

insert into search2photo(search_id, photo_id, create_time)
values (1, '12345', datetime('now')),
(1, '22345', datetime('now')),
(2, '32345', datetime('now')),
(2, '42345', datetime('now'));
