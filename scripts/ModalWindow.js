var showLoginWindow = function() {
	CODEBITS.loginWindow = new SAPO.Ink.Modal('#modalContent', {
		width:  500,
		height: 400
	});	
}

var dismissLoginWindow = function() {
	
	var name = CODEBITS.loginWindow.getContentElement().children[1].children[1].children[0].children[1].children[1].value;

	$("#title_content").replaceWith('<h1 id="title_content">Welcome ' + name + '</h1>');

	$('#name_field').val();
	CODEBITS.loginWindow.dismiss();

	$(dashboard_bt).replaceWith("<a href=\"#\" id=\"dashboard_bt\">Hi " + name + "</a>");
	prepareGalleryTabs();

	console.log("assd");

}

