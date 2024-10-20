$(document).ready(function() {
    // Function to fetch and display weather data
    function fetchWeather(city) {
        $.ajax({
            url: '/weather/',
            data: { city: city },
            success: function(data) {
                $('#weather-data').html(`
                    <h3>Weather in ${data.city}</h3>
                    <p class="weather-parameter">Temperature: ${data.temperature.toFixed(1)} °C</p>
                    <p class="weather-parameter">Feels Like: ${data.feels_like.toFixed(1)} °C</p>
                    <p class="weather-parameter">Humidity: ${data.humidity} %</p>
                    <p class="weather-parameter">Wind Speed: ${data.wind_speed} m/s</p>
                    <p class="weather-parameter">Condition: ${data.condition}</p>
                `).show(); // Show the weather data
            },
            error: function() {
                alert('Error fetching weather data. Please try again.');
            }
        });
    }

    // Fetch weather when form is submitted
    $('#weather-form').on('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const city = $('#city').val();
        fetchWeather(city); // Fetch weather data for the selected city
    });

    // Refresh button functionality
    $('#refresh-button').on('click', function() {
        const city = $('#city').val();
        fetchWeather(city); // Fetch weather data for the selected city
    });

    // Automatically refresh weather every 5 minutes
    setInterval(function() {
        const city = $('#city').val();
        fetchWeather(city);
    }, 300000); // 300000 ms = 5 minutes
});
