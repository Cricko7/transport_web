document.getElementById('station-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const frequency = document.getElementById('frequency').value;
    const location = document.getElementById('location').value;

    fetch('/add_station', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ frequency, location })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        this.reset();
    })
    .catch(error => console.error('Error:', error));
});
