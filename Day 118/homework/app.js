const film = document.querySelector('input');
        const movieDiv = document.getElementById('movieDiv');

        function movieFinder() {
            const filmValue = film.value;
            if (!filmValue) return;

            fetch(`https://api.themoviedb.org/3/search/movie?api_key=38c8a267e25940bf35aa75921cdd6af2&query=${encodeURIComponent(filmValue)}`)
                .then(res => res.json())
                .then(movie => {
                    const results = movie.results;
                    if (!results.length) {
                        movieDiv.innerHTML = '<p>No movies found.</p>';
                        return;
                    }

                    const movieData = results[0];

                    movieDiv.innerHTML = `
                        <h2 id='heading_2'>${movieData.original_title} (${movieData.release_date ? movieData.release_date.split('-')[0] : 'N/A'})</h2>
                        ${movieData.backdrop_path ? `<img id='img1' src='https://image.tmdb.org/t/p/w1280/${movieData.backdrop_path}' alt='Backdrop'>` : ''}
                        ${movieData.poster_path ? `<img src='https://image.tmdb.org/t/p/w400/${movieData.poster_path}' alt='Poster'>` : ''}
                        <button>Popularity: ${movieData.popularity}</button>
                        <p>${movieData.overview}</p>
                    `;
                })
                .catch(err => {
                    movieDiv.innerHTML = '<p>Error fetching movie data.</p>';
                    console.error(err);
                });
        }