const apiKey = "YOUR_API_KEY"

const url = `https://api.themoviedb.org/3/movie/popular?api_key=${apiKey}`

const container = document.getElementById("movies")

fetch(url)
.then(res => res.json())
.then(data => {

let movies = data.results

movies.forEach(movie => {

let div = document.createElement("div")
div.classList.add("movie")

div.innerHTML = `
<img src="https://image.tmdb.org/t/p/w400${movie.poster_path}">
<h3>${movie.title}</h3>
<p>⭐ ${movie.vote_average}</p>
<a href="movie.html?id=${movie.id}">details</a>
`

container.appendChild(div)

})

})