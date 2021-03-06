$(document).ready(function () {
    const anchors = document.querySelectorAll('a[href*="#"]')

    for (let anchor of anchors) {
        anchor.addEventListener('click', function (e) {
            e.preventDefault()

            const blockID = anchor.getAttribute('href').substr(1)

            document.getElementById(blockID).scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            })
        })
    }


    // Preloader
    setTimeout(function () {
        $('#preloader').fadeOut('slow', function () {
            $(this).remove();
        });
    }, 2000);

    // Img
    $("img, a").on("dragstart", function (event) {
        event.preventDefault();
    });


    // Scroll Header
    if ($(window).scrollTop() > 0) {
        $('.header').addClass('is-scroll');
    } else {
        $('.header').removeClass('is-scroll');
    }

    $(window).scroll(function () {

        if ($(window).scrollTop() > 0) {
            $('.header').addClass('is-scroll');
        } else {
            $('.header').removeClass('is-scroll');
        }

    });
    //Phone mask
    $('.phone-mask').mask('+38 (000) 000 00 00');


    // Page Scroll To ID
    // $(".scroll-link").mPageScroll2id({
    //     offset: 50
    // });


    // FAQ blocks
    $('.faq-block__toggle').click(function () {
        $(this).closest('.faq-block').toggleClass('on').find('.faq-block__hidden').slideToggle(500);
    });


    // Popup
    $("[data-fancybox]").fancybox({
        backFocus: false,
        centerOnScroll: true,
        toolbar: false,
        autoFocus: false,
        hideScrollbar: false
    });

    $('.popup__close').click(function () {
        parent.jQuery.fancybox.getInstance().close();
    });


    //Mobile Menu Toggle
    $('.menu-toggle').click(function () {
        $('.menu-toggle').toggleClass('on');
        $('.menu').toggleClass('is-visible');
    });

    const menu_toggle = document.querySelector('.menu-toggle');
    document.addEventListener('click', function (e) {
        const target = e.target;
        const toggle__1 = document.querySelector('.toggle__1');
        const toggle__2 = document.querySelector('.toggle__2');
        const toggle__3 = document.querySelector('.toggle__3');
        let flag = true;
        if (target === toggle__1 || target === toggle__2 || target === toggle__3 || target === menu_toggle) {
            flag = false;
        }
        if (flag && $('.menu-toggle').hasClass("on")) {
            $('.menu-toggle').toggleClass('on');
            $('.menu').toggleClass('is-visible');
        }
    });


    // Slider
    let swiper = new Swiper('.mySwiper', {
        slidesPerView: 1,
        autoplay: {
            delay: 4000,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            1200: {
                slidesPerView: 1,
            }
        }
    });

    let stepsSlider = new Swiper('.steps-slider', {
        spaceBetween: 0,
        slidesPerView: 1,
        loop: false,
        autoplay: {
            delay: 3000,
        },
        breakpoints: {
            0: {
                spaceBetween: 15,
                pagination: {
                    el: '.steps-slider-pagination',
                },
            },

            768: {
                spaceBetween: 0
            }
        }
    });

    stepsSlider.on('slideChange', function () {
        $('.steps-item').removeClass('is-active');
        $('.steps .steps-item:eq(' + stepsSlider.activeIndex + ')').addClass('is-active');
    });

    $('.steps-item').click(function () {
        let slide = parseInt($(this).data('slide'));
        stepsSlider.slideTo(slide - 1);
    });


    // Send Form
    $("[name = 'form_data_input']").submit(function (e) {
        e.preventDefault();
        phoneElement = $("#inputPhonePartner");
        if (phoneElement.val().length < 19) {
            return NaN
        }
        if (this.checkValidity()) {
            console.log(1);

            let data = $(this).serialize() + "&path=" + window.location.pathname;
            console.log(2);
            $.ajax({
                type: "POST",
                url: "/set_form",
                data: data
            }).done(function () {
                console.log(3);
                $.fancybox.close();
                $.fancybox.open($('#success-popup-partner'))

                setTimeout(function () {
                    $(".form").trigger("reset");
                }, 2000);
            });
            return false;
        }
    });


    $("[name = 'form_phone_input']").submit(function (e) {
        e.preventDefault();
        phoneElement = $("#inputPhone");
        if (phoneElement.val().length < 19) {
            return NaN
        }

        if (this.checkValidity()) {
            let data = $(this).serialize() + "&path=" + window.location.pathname;

            $.ajax({
                type: "POST",
                url: "/set_phone_form",
                data: data
            }).done(function () {

                $.fancybox.close();
                $.fancybox.open($('#success-popup'))

                setTimeout(function () {
                    $(".form").trigger("reset");
                }, 2000);
            });
            return false;
        }
    });


    $("[name = 'form_return_input']").submit(function (e) {
        if (!this.checkValidity()) {
            e.preventDefault();
        } else {
            let data = $(this).serialize() + "&path=" + window.location.pathname;

            $.ajax({
                type: "POST",
                url: "/set_return_form",
                data: data
            }).done(function () {

                $.fancybox.close();
                $.fancybox.open($('#success-popup'))

                setTimeout(function () {
                    $(".form").trigger("reset");
                }, 2000);
            });
            return false;
        }
    });

    let limit = 3;
    let offset = 6;

    $('#add-news-button').click(function () {
        $.ajax({
            type: "GET",
            url: `/api/news?limit=${limit}&offset=${offset}`,
        }).done(function (data) {
            let element = $('#news-row');
            data.results.forEach(news => {
                let html = `<div class="col-lg-4">
                                <div class="box-news">
                                    <a href="${news.url}">
                                        <picture class="box-news__picture">
                                            <img src="${news.img}" alt="news" class="box-news__img">
                                        </picture>
                                        <div class="box-news__descr">
                                            ${news.name}
                                        </div></a></div></div>`

                element.append(html);
            });
            if (data.next === null) {
                $('#add-news-button').hide();
            }
            offset += limit;
        });
    });


    $('#fb-buttton').click(function () {
        console.log('https://multioil.com.ua'+window.location.pathname.slice(0));
        window.open(`https://www.facebook.com/sharer.php?u=https://multioil.com.ua${window.location.pathname.slice(0)}`, 'sharer', 'status=0,toolbar=0,left=600,top=300,width=650,height=500');
    });
    $('#vb-buttton').click(function () {
        window.open(`viber://forward?text=${window.location.href}`, 'sharer', 'status=0,toolbar=0,left=600,top=300,width=650,height=500');
    });

    $('#tel-buttton').click(function () {
        window.open(`https://telegram.me/share/url?url=${window.location.href}`, 'sharer', 'status=0,toolbar=0,left=600,top=300,width=650,height=500');
    });

    $('#inst-buttton').click(function () {
        window.open(`https://telegram.me/share/url?url=${window.location.href}`, 'sharer', 'status=0,toolbar=0,left=600,top=300,width=650,height=500');
    });

})
;