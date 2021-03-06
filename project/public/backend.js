"use strict";

if( process.env.NODE_ENV !== 'staging' ){
	var httpProxy = require( 'http-proxy' );
	var apiProxy = httpProxy.createProxyServer();
	var spawn = require( 'child_process' ).spawn;
	var django = spawn( '/home/soo/wallabies/recipe-calorie-info/env/bin/python', ['../manage.py', 'runserver', '127.0.0.1:3000'] );

	console.log( 'django started on port 3000' );

	django.stdout.on( 'data', function( data ){
	 	console.log( data.toString() );
	} );

	django.stderr.on( 'data', function( data ){
	 	console.log( data.toString() );
	} );

	django.on( 'exit', function( code ){
		console.error( 'child process exited with code ' + code.toString() );
		console.error( 'Django failed to start, killing app' );
		process.exit();
	} );
};