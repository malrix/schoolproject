$('.mobile-nav').on('click', function (e) {
  e.preventDefault();
  $('.menu-button').toggleClass('menu-active')
  $('.main-menu').toggleClass('menu-active')
  $('.menu a').click(function(){$('.top_menu').slideUp(400);})
});