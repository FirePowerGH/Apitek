document.getElementById("fullname").addEventListener("input", function () {
    const query = this.value;
    if (query.length > 0) {
        fetch(`/register?q=${query}`)
            .then(response => response.json()) // Parse JSON from the response
            .then(data => {
                console.log("Parsed data:", data); // Debugging
                const dataList = document.getElementById("fullname-list");
                dataList.innerHTML = ""; // Clear previous options
                data.forEach(email => {
                    const option = document.createElement("option");
                    option.value = email;
                    dataList.appendChild(option);
                });
            })
            .catch(err => console.error("Error fetching names:", err));
    }
});
