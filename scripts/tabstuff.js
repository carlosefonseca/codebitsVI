var changeToGalleryTab = function (gallery_name, gallery_id) {

	$("#title_content").replaceWith('<h1 id="title_content">' + gallery_name + '</h1>');

	$("#main_container").replaceWith('<div class="ink-container" id="main_container" style="height:460px;">');
	if (gallery_name == undefined) {
		$("#main_container").append("<p>GALERIA TODA</p>");
	}
	else {
		//$("#main_container").append("<p>" + gallery_id  +  ": " + gallery_name + " </p>");	

		getPictures(gallery_id);

	}
}

var json_pictures = {};

var getPictures = function (gallery_id) {
	console.log("getting json for gallery " + gallery_id);
	$.getJSON("http://62.28.238.142:8088/album?id=" + gallery_id + "&callback=?",function(data){
		json_pictures = data.photos;
		//$("#main_container").append(generateGallery());
		generateGallery();
	});
}


var generateGallery = function (from) {
	var counter = 0;


	if (from != undefined)
		counter = from;

	console.log("Starting from " + counter);


	$("#main_container").replaceWith('<div class="ink-container" id="main_container" style="height:460px;">');
	$("#pagination_ul").replaceWith('<ul class="pagination" id="pagination_ul">');
	var size = json_pictures.length;
	var n_cols = 0;
	var n_rows = 0;
	var max_cols = 5;
	var max_rows = 4;

	var newMax = counter+(max_cols*max_rows);
	
	if (size > max_cols) {
		if (size > (max_cols*max_rows)) {
			n_cols = max_cols;
			n_rows = max_rows;
		}
		else {
			n_cols = max_cols;
			n_rows =  Math.ceil(size/max_cols);
		}
	} else {
		n_cols = max_cols;
		n_rows = 1;
	}

	//

	var needed_screens = Math.ceil(size/(max_cols*max_rows));

	for (var k=1; k<=needed_screens; k+=1) {
		$("#pagination_ul").append('<li><a href="javascript:generateGallery(' + (((k-1)*(max_cols*max_rows))-1) + ');">' + k + '</a></li>');
	}

	console.log("N cols: " + n_cols + " n rows: " + n_rows);

	var percent = (1/n_cols)*100;


	for (;counter<newMax; counter+=1) {
		var picture = json_pictures[counter];
		console.log("getting picture " + counter);
		if (picture != undefined) {
			//aux = '<div class="ink-gutter"><p>iuiu</p></div>';

			aux = '<img src="' + picture.url + '" style="max-width:95%; max-height:95%;"></img>';
		}
		var column = '<div class="ink-l' + percent + '">' + aux + '</div>';

		console.log("creating column: " + column);

		$("#main_container").append(column);


	}

/*

	for (var i=0; i<n_rows; i+=1) {
		//var row = '<div class="ink-row" id="gr' + i + '">';
		//$("#main_container").append(row);


		for (var j=0; j<n_cols; j++, counter+=1) {

			console.log("getting picture " + counter);
			var aux = "<p></p>";
			var picture = json_pictures[counter];

			if (picture != undefined) {
			//aux = '<div class="ink-gutter"><p>iuiu</p></div>';
			aux = '<img src="' + picture.url + '" style="max-width:95%; max-height:95%;"></img>';
		}

		var column = '<div class="ink-l' + percent + '">' + aux + '</div>';

		console.log("creating column: " + column);

		$("#main_container").append(column);

	}
	
} */



}

/*

var generateGallery = function() {

	var str =  '<ul class="ink-gallery-source">' + getGalleryPicturesCode() + '</ul><script type="text/javascript">var gal2 = new SAPO.Ink.Gallery(".ink-gallery-source", {layout:2});</script>';
	console.log("Items: " + str);
	return str;
}

var getGalleryPicturesCode = function(){
	var size = json_pictures.length;
	console.log("Size: " + size);
	var code = "";
	for (var i=0; i<size; i=i+1) {
		console.log("lalalalala " + i);
		code = code + getPictureCode(i);
	}
	return code;
}

var getPictureCode = function(position) {	
	var picture = json_pictures[position];

	var original_text = '<li class="hentry hmedia"><a rel="enclosure" href="'+ picture.source_url + '"><img alt="s1" src="' + picture.thumb_url + '"></a><a class="bookmark" href="http://imgs.sapo.pt/ink/assets/imgs_gal/1.1.png"><span class="entry-title">s1</span></a><span class="entry-content"><p>hello world 1</p></span></li>';

	console.log("Adding: " + original_text);

	return original_text;
}

*/






/*
<ul class="ink-gallery-source">
    <li class="hentry hmedia">
        <a rel="enclosure" href="http://imgs.sapo.pt/ink/assets/imgs_gal/1.1.png">
            <img alt="s1" src="http://imgs.sapo.pt/ink/assets/imgs_gal/thumb1.png">
        </a>
        <a class="bookmark" href="http://imgs.sapo.pt/ink/assets/imgs_gal/1.1.png">
            <span class="entry-title">s1</span>
        </a>
        <span class="entry-content"><p>hello world 1</p></span>
    </li>
    <li class="hentry hmedia">
        <a rel="enclosure" href="http://imgs.sapo.pt/ink/assets/imgs_gal/1.2.png">
            <img alt="s1" src="http://imgs.sapo.pt/ink/assets/imgs_gal/thumb2.png">
        </a>
        <a class="bookmark" href="http://imgs.sapo.pt/ink/assets/imgs_gal/1.2.png">
            <span class="entry-title">s2</span>
        </a>
        <span class="entry-content"><p>hello world 2</p></span>
    </li>
</ul>
<script type="text/javascript">
    var gal2 = new SAPO.Ink.Gallery('.ink-gallery-source', {layout:2});
</script>

*/




var changeToMainTab = function () {
	$("#main_container").replaceWith('<div class="ink-l100" id="main_container" style="height:500px">');
}

var changeToHelpTab = function () {
	$("#main_container").replaceWith('<div class="ink-l100" id="main_container" style="height:500px">');
}

var changeToSettingsTab = function () {
	$("#main_container").replaceWith('<div class="ink-l100" id="main_container" style="height:500px">');
}

