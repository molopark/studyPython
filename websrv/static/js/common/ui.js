$(function() {

	$(".tabs > li").click(function(){
		var tabs = $(this);
		var activeTab = tabs.attr("rel");
		var tabct = $(this).parent().next('.tabCt');
		tabs.addClass("active").siblings().removeClass("active");
		tabct.children('.tabUnit').hide();
		$("#" + activeTab).show();
	});

	 $(".collaps").each(function(i) {
		var collaps = $(this);
		collaps.find(".clpsTit").click(function(){			
			collaps.toggleClass('open');
		});
	 });

	 $('.check-box').each(function(i) {
		var checkbox = $(this);
		checkbox.find('.checkTit').change(function(){
			checkbox.find('.checkCt').toggle();		
			checkbox.toggleClass('open');	
		});
	});


	 $(".menuBtn").click(function(){
		var menu = $(this);
		menu.toggleClass("on");
		menu.closest("body").toggleClass("menuOpen");
	});
		

  
});