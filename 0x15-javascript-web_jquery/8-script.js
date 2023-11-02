$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $('ul#list_movies').html(
    data.results.map((x) => '<li>' + x.title + '</li>').join('')
  );
});
