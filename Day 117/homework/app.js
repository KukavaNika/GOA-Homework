const apiKey = "YOUR_API_KEY"

const btn = document.getElementById("searchBtn")
const input = document.getElementById("searchInput")
const container = document.getElementById("movies")

btn.addEventListener("click", function(){

let movieName = input.value

let url = `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${movieName}`

fetch(url)
.then(res => res.json())
.then(data => {

container.innerHTML = ""

data.results.forEach(movie => {

let div = document.createElement("div")
div.classList.add("movie")

div.innerHTML = `
<img src="https://image.tmdb.org/t/p/w400${movie.poster_path}">
<h3>${movie.title}</h3>
<p>⭐ ${movie.vote_average}</p>
`

container.appendChild(div)

})

})

})