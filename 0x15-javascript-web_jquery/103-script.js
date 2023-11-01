$(docunent).ready(function () {
  function translate () {
    $('#hello').empty();
    const len = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/?lang=' + len,
      success: function (data) {
        $('#hello').append(data.hello);
      }
    });
  }
  $('#btn_translate').click(function () {
    translate();
  });
  $('#language_code').keypress(function (e) {
    const key = e.which;
    if (key === 13) {
      translate();
    }
  });});
