async function loadData() {
    const response = await fetch("http://127.0.0.1:5000/dashboard");
    const data = await response.json();

    document.getElementById("suppliers").innerText = data.suppliers;
    document.getElementById("orders").innerText = data.orders;
    document.getElementById("delivery").innerText = data.delivery;
}

loadData();