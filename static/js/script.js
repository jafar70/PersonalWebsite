// JavaScript File
$(document).ready(function(){
    var amountScrolled = 300;

    $(window).scroll(function() {
    	if ( $(window).scrollTop() > amountScrolled ) {
    		$('a.back-to-top').fadeIn('slow');
    	} else {
    		$('a.back-to-top').fadeOut('slow');
    	}
    });
    
    $('a.back-to-top').click(function() {
    	$('html, body').animate({
    		scrollTop: 0
    	}, 700);
    	return false;
    });
    
    jQuery(function () {
    jQuery('#myTab a:last').tab('show')
});
});

$(document).ready(function(){
	
	$('ul.tabs li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})
	
	$("#toaboutme").click(function() {
    $('html, body').animate({
        scrollTop: $("#aboutme").offset().top - 50
    }, 2000);
    });
    
    $('#mainNav').affix({
      offset: {
        top: 100
      }
    })
    
    $(document).scroll(function(){
    if($(this).scrollTop() > 50)
    {   
       $('.navbar-inverse .navbar-brand').css({"font-size":"21px"});
    } else {
       $('.navbar-inverse .navbar-brand').css({"font-size":"2em"});
    }
});
})


