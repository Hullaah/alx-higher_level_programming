$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(() => $(this).keydown(translate));
  function translate (e) {
    const language = $('INPUT#language_code').val();
    if (!e.key || e.key === 'Enter') {
      const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language;
      $.get(url,
        function (data) {
          $('DIV#hello').html(data.hello);
        }
      );
    }
  }
});
