$(function () {
    let $lang = $('div#hello')
    $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function (data) {
            $lang.append('<p>' + lang.hello + '.</p>');
        }
    });
});
