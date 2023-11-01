$('DIV#add_item').bind('click', function (e) {
  let ul = $('UL.my_list').html();
  ul += '<li>Item</li>';
  $('UL.my_list').html(ul);
});
