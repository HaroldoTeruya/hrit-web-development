$(document).ready(function()
{
  $(window).load(function()
  {
    $(".wrapper").removeClass("nopre");
  });

  $('#container > div').click(function(){
    if ($('#container').attr('class') == $(this).attr('id')) {
      $('#container').removeClass();
    } else {
      $('#container').removeClass().addClass($(this).attr('id'));
    }
  });

  $('#container > div > ul').click(function(e){
    e.stopPropagation();
  });

  $(window).scroll(function ()
  {
    var position = $(window).scrollTop();
    var element = $("#sidebar-logo");
    if( position < 300 && element.css('opacity') == 1 )
    {
      element.animate({
        opacity: 0
      }, 250, function() {
      });
    }
    else if( position >= 300 && element.css('opacity') == 0 )
    {
      element.animate({
        opacity: 1
      }, 250, function() {
      });
    }
  });
});
