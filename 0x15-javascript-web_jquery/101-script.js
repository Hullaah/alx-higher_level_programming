function documentReady () {
  $('DIV#remove_item').bind('click', function (e) {
    let ul = $('ul.my_list').html();
    const lastItem = ul.lastIndexOf('<li>');
    ul = ul.slice(0, lastItem);
    $('ul.my_list').html(ul);
  });
  $('DIV#add_item').bind('click', function (e) {
    let ul = $('ul.my_list').html();
    if (ul) {
      const lastItem = ul.lastIndexOf('<li>');
      ul += ul.slice(0, lastItem);
      $('ul.my_list').html(ul);
    } else {
      $('ul.my_list').html('<li>Item</li>');
    }
  });
  $('DIV#clear_list').bind('click', function (e) {
    $('ul.my_list').html('');
  });
}
$(document).ready(documentReady);
