const key = "1fab308981764501b85c1a214ded4756";
const city = "Sudan";

fetch(`https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${key}&units=metric`)
    .then(res => {
        if (!res.ok) throw new Error("Network response was not ok");
        return res.json();
    })
    .then(data => console.log(`Current temperature in ${city}: ${data.main.temp}°C`))
    .catch(err => console.error("Error fetching weather data:", err));