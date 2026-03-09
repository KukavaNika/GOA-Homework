  const film = document.querySelector('#film');
        const movieDiv = document.querySelector('#movieDiv');
        const searchBtn = document.querySelector('#searchBtn');

        function movieFinder() {
            const filmValue = film.value.trim();
            if (!filmValue) return;
            movieDiv.innerHTML = 'Loading...';

            fetch(`https://api.themoviedb.org/3/search/movie?api_key=38c8a267e25940bf35aa75921cdd6af2&query=${encodeURIComponent(filmValue)}`)
                .then(res => res.json())
                .then(data => {
                    const movies = data.results;
                    if (!movies.length) {
                        movieDiv.innerHTML = 'No movies found.';
                        return;
                    }

                    movieDiv.innerHTML = movies.map(movie => {
                        if (movie.poster_path) {
                            return `<img src="https://image.tmdb.org/t/p/w400/${movie.poster_path}" alt="${movie.title}">`;
                        } else {
                            return `<p>${movie.title} (No image)</p>`;
                        }
                    }).join('');
                })
                .catch(err => {
                    movieDiv.innerHTML = 'Error fetching movies.';
                    console.error(err);
                });
        }

        searchBtn.addEventListener('click', movieFinder);
        film.addEventListener('keypress', e => {
            if (e.key === 'Enter') movieFinder();
        });