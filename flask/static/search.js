const nameInput = document.getElementById('fullname');
const nameList = document.getElementById('fullname-list');

nameInput.addEventListener('input', () => {
    const query = nameInput.value;

    if (query.length > 0) {
        // Fetch email suggestions from Flask backend
        fetch(`/register?q=${query}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        })
            .then(response => {
                console.log('Response status:', response.status);
                console.log('Response headers:', response.headers);
                return response.json();
            })
            .then(data => {
                nameList.innerHTML = ''; // Clear existing options
                data.forEach(fullname => {
                    const option = document.createElement('option');
                    option.value = fullname;
                    nameList.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Error fetching names:', error);
                console.error('Response:', error.response);
            });
    } else {
        nameList.innerHTML = '';
    }});
    