// Generated by CoffeeScript 1.3.3
(function() {
  var index;

  index = '\
<!doctype html>\
<html lang="en">\
	<head>\
		<meta charset="utf-8">\
		<title>{{ pageTitle }}</title>\
\
		<link rel="stylesheet" href="/css/main.css">\
\
		{{#css}}\
			<link rel="stylesheet" href="{{ cssPath }}{{ cssFileName }}{{ cssVersion }}">\
		{{/css}}\
\
		<!--[if lt IE 9]>\
			<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>\
		<![endif]-->\
	</head>\
	<body>\
		{{{ template }}}\
\
		{{#js}}\
			<script src="{{ jsPath }}{{ jsFileName }}{{ jsVersion }}"></script>\
		{{/js}}\
	</body>\
</html>\
';

  module.exports = index;

}).call(this);