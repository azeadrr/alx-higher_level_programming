$(function () {
    let $titles = $('ul#list_movies')
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function (titles) {
            var index = 0
            $.each(titles, function (idx, title) {
                $titles.append('<li> title :' + titles.results[index].title + '.</li>');
                index = index + 1;
            });
        }
    });
});
