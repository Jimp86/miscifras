jQuery(document).ready(function ($) {

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });
  $('.back-to-top').click(function () {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Stick the header at top on scroll
  $("#header").sticky({
    topSpacing: 0,
    zIndex: '50'
  });

  // Intro background carousel
  $("#intro-carousel").owlCarousel({
    autoplay: true,
    dots: false,
    loop: true,
    animateOut: 'fadeOut',
    items: 1
  });

  // Slider Noticias
  var img_noticias = $('.slider-noticias').length;
  console.log(img_noticias);

  for(i = 1; i <=img_noticias; i++){
      $('.pagination').append('<li><span class="fa fa-circle"></span></li>');
  }

  $('.pagination').append('<li><span class="fa fa-circle"></span></li>');


  $('.slider-noticias').hide();
  $('.slider-noticias:first').show();
  $('.pagination li:first').css({'color':'#50d8af'});

  $('.more-post').hide();
  $('.more-post:first').show();
  $('.news-list-item:first').hide();

  //
  //$('.pagination li').click(pagination);
  //$('.left span').click(prevSlider);
  //$('.right span').click(nextSlider);

  //
  //function pagination(){
      //var = pagpos = $(this).index() + 1;//*--posicion paginacion--*/

      //$('.slider-noticias').hide();
      //$('.slider-noticias:nth-child(' + pagpos +')').fadeIn();
  //}

  //function left(){
      //if(imgPos <= 1){imgPos = imgItems;}
      //else{imgPos--;}
      //$('.pagination li').css({'color':'#858585'});
      //$('.pagination li:nth-child('+ imgPos +')').css({'color':'#ffff'});
      //$('.slider li').hide();
      //$('.slider li:nth-child('+ imgPos +')').fadeIn();

  // Slider About

  //var imgItems = $('.slider li').length;
  //var imgPos = 1;

  //for(i = 1; i <=imgItems; i++){
      //$('.pagination').append('<li><span class="fa fa-circle"></span></li>');
  //}

  //$('.slider li').hide();
  //$('.slider li:first').show();
  //$('.pagination li:first').css({'color': '#ffff'});

  //$('.pagination li').click(pagination);
  //$('.prev a').click(prevSlider);
  //$('.next a').click(nextSlider);

  //setInterval(function (){
      //nextSlider();
  //},9000);

  //function pagination(){
      //var paginationPos = $(this).index() + 1;
      //$('.slider li').hide();
      //$('.slider li:nth-child('+ paginationPos +')').fadeIn();
      //$('.pagination li').css({'color':'#858585'})
      //$(this).css({'color':'#ffff'});
  //}

  //function pagination(){
      //var paginationPos = $(this).index() + 1;
      //$('.slider li').hide();
      //$('.slider li:nth-child('+ paginationPos +')').fadeIn();
      //$('.pagination li').css({'color':'#858585'});
      //$(this).css({'color':'#ffff'});
      //imgPos = paginationPos;
  //}

  //function prevSlider(){
      //if(imgPos <= 1){imgPos = imgItems;}
      //else{imgPos--;}
      //$('.pagination li').css({'color':'#858585'});
      //$('.pagination li:nth-child('+ imgPos +')').css({'color':'#ffff'});
      //$('.slider li').hide();
      //$('.slider li:nth-child('+ imgPos +')').fadeIn();
  //}

  //function nextSlider(){
      //if(imgPos >= imgItems){imgPos = 1;}
      //else{imgPos++;}
      //$('.pagination li').css({'color':'#858585'});
      //$('.pagination li:nth-child('+ imgPos +')').css({'color':'#ffff'});
      //$('.slider li').hide();
      //$('.slider li:nth-child('+ imgPos +')').fadeIn();
  //}


  // Initiate the wowjs animation library
  new WOW().init();

  // Initiate superfish on nav menu
  $('.nav-menu').superfish({
    animation: {
      opacity: 'show'
    },
    speed: 400
  });

  // Mobile Navigation
  if ($('#nav-menu-container').length) {
    var $mobile_nav = $('#nav-menu-container').clone().prop({
      id: 'mobile-nav'
    });
    $mobile_nav.find('> ul').attr({
      'class': '',
      'id': ''
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" id="mobile-nav-toggle"><i class="fa fa-bars"></i></button>');
    $('body').append('<div id="mobile-body-overly"></div>');
    $('#mobile-nav').find('.menu-has-children').prepend('<i class="fa fa-chevron-down"></i>');

    $(document).on('click', '.menu-has-children i', function (e) {
      $(this).next().toggleClass('menu-item-active');
      $(this).nextAll('ul').eq(0).slideToggle();
      $(this).toggleClass("fa-chevron-up fa-chevron-down");
    });

    $(document).on('click', '#mobile-nav-toggle', function (e) {
      $('body').toggleClass('mobile-nav-active');
      $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
      $('#mobile-body-overly').toggle();
    });

    $(document).click(function (e) {
      var container = $("#mobile-nav, #mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
      }
    });
  } else if ($("#mobile-nav, #mobile-nav-toggle").length) {
    $("#mobile-nav, #mobile-nav-toggle").hide();
  }

  // Smooth scroll for the menu and links with .scrollto classes
  $('.nav-menu a, #mobile-nav a, .scrollto').on('click', function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        var top_space = 0;

        if ($('#header').length) {
          top_space = $('#header').outerHeight();

          if (!$('#header').hasClass('header-fixed')) {
            top_space = top_space - 20;
          }
        }

        $('html, body').animate({
          scrollTop: target.offset().top - top_space
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu').length) {
          $('.nav-menu .menu-active').removeClass('menu-active');
          $(this).closest('li').addClass('menu-active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
        return false;
      }
    }
  });


  // Porfolio - uses the magnific popup jQuery plugin
  $('.portfolio-popup').magnificPopup({
    type: 'image',
    removalDelay: 300,
    mainClass: 'mfp-fade',
    gallery: {
      enabled: true
    },
    zoom: {
      enabled: true,
      duration: 300,
      easing: 'ease-in-out',
      opener: function (openerElement) {
        return openerElement.is('img') ? openerElement : openerElement.find('img');
      }
    }
  });

  // Testimonials carousel (uses the Owl Carousel library)
  $(".testimonials-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    responsive: {
      0: {
        items: 1
      },
      768: {
        items: 2
      },
      900: {
        items: 3
      }
    }
  });

  // Clients carousel (uses the Owl Carousel library)
  $(".clients-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    responsive: {
      0: {
        items: 2
      },
      768: {
        items: 4
      },
      900: {
        items: 6
      }
    }
  });


});

/*========login & Register ========*/

(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);