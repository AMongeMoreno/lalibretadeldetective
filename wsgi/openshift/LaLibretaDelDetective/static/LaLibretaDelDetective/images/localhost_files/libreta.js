$(function() {
    //single book
    var book = $('#mybook').booklet({
    	closed:true,
    	covers: true,
    	arrows: true,
    	autoCenter:true,
    	hovers:false,
    	manual:false,
    	width: '939px',
    	height: '840px',
    	chapterSelector: true,
		menu:"#custom-menu",
    	});    
    	
    $(".b-div-cover-back").parent().addClass('b-page-cover-back');
    $(".b-div-cover-front").parent().addClass('b-page-cover-front');
});
