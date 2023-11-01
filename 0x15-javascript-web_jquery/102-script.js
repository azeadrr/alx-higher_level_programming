$(document).ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/'
    $('input#btn_translate').click(function () {
        const lan = $('input#language_code').val();
        $.get(url + $.param({ lan }), function (data) {
            $('div#hello').html(data.hello);
        });
    });
});
