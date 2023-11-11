const citiesField = document.querySelector('#id_cities');
const regionsField = document.querySelector('#id_regions');

regionsField.addEventListener('change', (e) => {
    const regionId = e.target.value;
    const url = `/get_cities/?region_id=${regionId}`;

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            citiesField.innerHTML = '';
            data.forEach((city) => {
                const option = document.createElement('option');
                option.value = city.id;
                option.textContent = city.name;
                citiesField.appendChild(option);
            });
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});