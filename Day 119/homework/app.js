 const apiKey = "1fab308981764501b85c1a214ded4756";
        const cityInput = document.getElementById('cityInput');
        const getWeatherBtn = document.getElementById('getWeatherBtn');
        const weatherDiv = document.getElementById('weatherDiv');

        function fetchWeather() {
            const city = cityInput.value.trim();
            if (!city) return;
            weatherDiv.innerHTML = 'Loading...';

            fetch(`https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`)
                .then(res => {
                    if (!res.ok) throw new Error('City not found');
                    return res.json();
                })
                .then(data => {
                    const temp = data.main.temp;
                    const description = data.weather[0].description;

                    weatherDiv.innerHTML = `
                        <h2>${city}</h2>
                        <p>Temperature: ${temp}°C</p>
                        <p>Weather: ${description}</p>
                    `;
                })
                .catch(err => {
                    weatherDiv.innerHTML = `<p>Error: ${err.message}</p>`;
                });
        }

        getWeatherBtn.addEventListener('click', fetchWeather);
        cityInput.addEventListener('keypress', e => {
            if (e.key === 'Enter') fetchWeather();
        });

fetchWeather();