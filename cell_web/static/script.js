document.getElementById('station-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const frequency = document.getElementById('frequency').value;
    const location = document.getElementById('location').value;
    const latitude = parseFloat(document.getElementById('latitude').value);
    const longitude = parseFloat(document.getElementById('longitude').value);

    // Валидация координат
    if (latitude < -90 || latitude > 90 || longitude < -180 || longitude > 180) {
        alert("Пожалуйста, введите корректные координаты.");
        return;
    }

    fetch('/add_station', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ frequency, location, latitude, longitude })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        
        // Добавляем новую станцию в список на странице
        const stationList = document.getElementById('station-list');
        const newStation = document.createElement('li');
        newStation.textContent = `Частота: ${frequency}, Расположение: ${location}`;
        
        // Добавляем маркер на карту
        const marker = L.marker([latitude, longitude]).addTo(map)
            .bindPopup(`Частота: ${frequency}<br>Расположение: ${location}`);
        
        // Добавляем кнопку удаления для новой станции
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Удалить';
        deleteButton.onclick = function() {
            fetch(`/delete_station/${data.id}`, { method: 'DELETE' })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);
                    map.removeLayer(marker); // Удаляем маркер с карты
                    stationList.removeChild(newStation); // Удаляем элемент из списка
                });
        };
        
        newStation.appendChild(deleteButton);
        stationList.appendChild(newStation);
        
        this.reset(); // Сбрасываем_форму
    })
    .catch(error => console.error('Error:', error));
});
