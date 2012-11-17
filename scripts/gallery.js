var jsonGallery = {};
var currentVal = {};

var prepareGalleryTabs = function (){

	//jsonGallery = $.getJSON("http://62.28.238.142:8088/album?id=123&callback=?",function(data){
		jsonGallery = $.getJSON("http://62.28.238.142:8088/albums?callback=?",function(data){
			jsonGallery = data;

			jQuery.each(jsonGallery, function(i, val) {
				addTabs(val);
			});

		});
}

var addTabs = function(gallery) {
	var name = gallery.name;
	var id = gallery.id;
	console.log(name);
	$("#gallery_submenus").append("<li><a href='javascript:changeToGalleryTab(\""+ name+ "\", \"" + id + "\");'>" + gallery.name + "</a></li>");
}


