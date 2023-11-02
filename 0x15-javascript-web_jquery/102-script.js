$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  function translate (e) {
    const language = $('INPUT#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language;
    $.get(url,
      function (data) {
        $('DIV#hello').html(data.hello);
      }
    );
  }
});
