$(function () {
    // ================================================
    //  NAVBAR BEHAVIOR
    // ================================================
    $(window).on('scroll load', function () {
        if ($(window).scrollTop() > 5) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });

    // ================================================
    // Preventing URL update on navigation link click
    // ================================================
    $('.link-scroll').on('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top
        }, 1000);
        e.preventDefault();

        $('.navbar-collapse.collapse').toggleClass('show');
    });

    // ================================================
    //  TESTIMONIALS SLIDER
    // ================================================
    $('.testimonials-slider').owlCarousel({
        items: 1,
        dots: true
    });

    // ================================================
    // Scroll Spy
    // ================================================
    $('body').scrollspy({
        target: '#navbarSupportedContent',
        offset: 80
    });


    alert('Hello');

});
