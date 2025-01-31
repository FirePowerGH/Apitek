document.getElementById("fullname").addEventListener("input", function () {
    const nameValue = this.value.trim();
    const query = this.value;
    if (query.length > 0) {
        fetch(`/register?q=${query}`)
            .then(response => response.json())
            .then(data => {
                const dataList = document.getElementById("fullname-list");
                dataList.innerHTML = "";
                data.forEach(name => {
                    const option = document.createElement("option");
                    option.value = name.join(" ");
                    dataList.appendChild(option);
                    console.log(name)
                });
            })
            .catch(err => console.error("Error fetching names:", err));
    }
    if (nameValue.length > 0) {
        document.getElementById("userpass").style.display = "block";
    } else {
        document.getElementById("userpass").style.display = "none";
    }
});
