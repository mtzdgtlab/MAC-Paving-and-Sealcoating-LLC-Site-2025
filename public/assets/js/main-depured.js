(function ($) {
  'use strict';

  // Preloader
  $(window).on('load', function () {
    $('#preloader').delay(500).fadeOut(500);
  });

  // Button hover effect
  $('.btn-hover')
    .on('mouseenter', function (e) {
      const offset = $(this).offset();
      const relX = e.pageX - offset.left;
      const relY = e.pageY - offset.top;
      $(this).find('span').css({ top: relY, left: relX });
    })
    .on('mouseout', function (e) {
      const offset = $(this).offset();
      const relX = e.pageX - offset.left;
      const relY = e.pageY - offset.top;
      $(this).find('span').css({ top: relY, left: relX });
    });

  // Mobile menus
  $('#mobile-menu').meanmenu({
    meanMenuContainer: '.mobile-menu',
    meanScreenWidth: '991',
    meanExpand: ['<i class="fas fa-plus"></i>'],
  });
  $('#mobile-menu-2').meanmenu({
    meanMenuContainer: '.mobile-menu-2',
    meanScreenWidth: '4000',
    meanExpand: ['<i class="fas fa-plus"></i>'],
  });

  // Sidebar
  $('.offcanvas__close,.offcanvas__overlay').on('click', function () {
    $('.offcanvas__info').removeClass('info-open');
    $('.offcanvas__overlay').removeClass('overlay-open');
  });
  $('.sidebar__toggle').on('click', function () {
    $('.offcanvas__info').addClass('info-open');
    $('.offcanvas__overlay').addClass('overlay-open');
  });

  // Body overlay
  $('.body-overlay').on('click', function () {
    $('.offcanvas__area').removeClass('offcanvas-opened');
    $('.df-search-area').removeClass('opened');
    $('.body-overlay').removeClass('opened');
  });

  // Sticky header
  $(window).on('scroll', function () {
    $('#header-sticky').toggleClass('sticky', $(this).scrollTop() > 250);
  });

  // Data attributes
  $('[data-background]').each(function () {
    $(this).css('background-image', 'url(' + $(this).attr('data-background') + ')');
  });
  $('[data-width]').each(function () {
    $(this).css('width', $(this).attr('data-width'));
  });
  $('[data-bg-color]').each(function () {
    $(this).css('background-color', $(this).attr('data-bg-color'));
  });

  // Popups
  $('.popup-image').magnificPopup({
    type: 'image',
    gallery: { enabled: true },
  });
  $('.popup-video').magnificPopup({ type: 'iframe' });

  // Counters
  $('.counter').counterUp({ delay: 10, time: 1000 });

  // AOS animations
  AOS.init({ duration: 600, easing: 'ease-in-out', once: true, offset: 100 });

  // Current year in footer
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // Back to top
  const progressPath = document.querySelector('.backtotop-wrap path');
  if (progressPath) {
    const pathLength = progressPath.getTotalLength();
    progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
    progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
    progressPath.style.strokeDashoffset = pathLength;
    progressPath.getBoundingClientRect();
    progressPath.style.transition =
      progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
    const updateProgress = function () {
      const scroll = $(window).scrollTop();
      const height = $(document).height() - $(window).height();
      const progress = pathLength - (scroll * pathLength) / height;
      progressPath.style.strokeDashoffset = progress;
    };
    updateProgress();
    $(window).scroll(updateProgress);
    const offset = 150;
    const duration = 550;
    $(window).on('scroll', function () {
      $('.backtotop-wrap').toggleClass('active-progress', $(this).scrollTop() > offset);
    });
    $('.backtotop-wrap').on('click', function (event) {
      event.preventDefault();
      $('html, body').animate({ scrollTop: 0 }, duration);
    });
  }

  // Swiper sliders
  new Swiper('.testimonial-active-2', {
    slidesPerView: 2,
    spaceBetween: 20,
    loop: true,
    roundLengths: true,
    autoplay: { delay: 3000 },
    pagination: { el: '.testimonial-swiper-dot', clickable: true },
    navigation: {
      nextEl: '.testimonial-button-next',
      prevEl: '.testimonial-button-prev',
    },
    breakpoints: {
      1400: { slidesPerView: 2 },
      1200: { slidesPerView: 2 },
      992: { slidesPerView: 2 },
      768: { slidesPerView: 1 },
      576: { slidesPerView: 1 },
      0: { slidesPerView: 1 },
    },
  });

  new Swiper('.brand-active', {
    slidesPerView: 4,
    spaceBetween: 99,
    loop: true,
    roundLengths: true,
    autoplay: { delay: 3000 },
    breakpoints: {
      1400: { slidesPerView: 4 },
      1200: { slidesPerView: 3 },
      992: { slidesPerView: 3 },
      768: { slidesPerView: 2 },
      576: { slidesPerView: 2 },
      0: { slidesPerView: 1 },
    },
    speed: 1000,
  });

  new Swiper('.project-active-1', {
    slidesPerView: 2,
    spaceBetween: 30,
    loop: true,
    autoplay: { delay: 2000 },
    navigation: {
      nextEl: '.project-1-button-next',
      prevEl: '.project-1-button-prev',
    },
    breakpoints: {
      1400: { slidesPerView: 4 },
      1200: { slidesPerView: 3 },
      992: { slidesPerView: 2 },
      768: { slidesPerView: 2 },
      576: { slidesPerView: 1 },
      0: { slidesPerView: 1 },
    },
    speed: 1000,
  });

  new Swiper('.service-active-1', {
    slidesPerView: 2,
    spaceBetween: 30,
    loop: true,
    roundLengths: true,
    autoplay: { delay: 2000 },
    navigation: {
      nextEl: '.service-1-button-next',
      prevEl: '.service-1-button-prev',
    },
    breakpoints: {
      1400: { slidesPerView: 2 },
      1200: { slidesPerView: 2 },
      992: { slidesPerView: 2 },
      768: { slidesPerView: 1 },
      576: { slidesPerView: 1 },
      0: { slidesPerView: 1 },
    },
    speed: 1500,
  });

  if ($('.banner-active').length > 0) {
    const sliderActive = '.banner-active';
    const sliderInit = new Swiper(sliderActive, {
      slidesPerView: 1,
      slidesPerColumn: 1,
      paginationClickable: true,
      fadeEffect: { crossFade: true },
      loop: true,
      effect: 'fade',
      autoplay: { delay: 5000 },
      navigation: {
        nextEl: '.slider__button-next',
        prevEl: '.slider__button-prev',
      },
      pagination: { el: '.banner-dot', clickable: true },
      a11y: false,
    });
    const animate = function () {
      $(sliderActive + ' [data-animation]').each(function () {
        const anim = $(this).data('animation');
        const delay = $(this).data('delay');
        const duration = $(this).data('duration');
        $(this)
          .removeClass('anim' + anim)
          .addClass(anim + ' animated')
          .css({
            webkitAnimationDelay: delay,
            animationDelay: delay,
            webkitAnimationDuration: duration,
            animationDuration: duration,
          })
          .one(
            'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
            function () {
              $(this).removeClass(anim + ' animated');
            }
          );
      });
    };
    animate();
    sliderInit.on('slideChange', function () {
      $(sliderActive + ' [data-animation]').removeClass('animated');
    });
    sliderInit.on('slideChange', animate);
  }
})(jQuery);