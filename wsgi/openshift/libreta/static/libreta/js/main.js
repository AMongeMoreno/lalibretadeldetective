$(function() {
    //single book
    var book = $('#mybook').booklet({
    	closed:true,
    	covers: true,
    	arrows: true,
    	autoCenter:true,
    	width: 780,
    	height: 600,
    	});    
    	
    $(".b-div-cover-back").parent().addClass('b-page-cover-back');
    $(".b-div-cover-front").parent().addClass('b-page-cover-front');
});
