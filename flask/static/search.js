const nameInput = document.getElementById('fullname');
const nameList = document.getElementById('fullname-list');

nameInput.addEventListener('input', () => {
    const query = nameInput.value;

    // Fetch email suggestions from Flask backend
    fetch(`/register?q=${query}`)
        .then(response => response.json())
        .then(data => {
            nameList.innerHTML = ''; // Clear existing options
            data.forEach(fullname => {
                const option = document.createElement('option');
                option.value = fullname;
                nameList.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching names:', error));
});