async function loadData() {

    const response =
        await fetch("http://127.0.0.1:5000/dashboard");

    const data =
        await response.json();

    document.getElementById("suppliers").innerText =
        data.suppliers;

    document.getElementById("orders").innerText =
        data.orders;

    document.getElementById("delivery").innerText =
        data.delivery + "%";

    const labels =
        data.risk_analysis.map(
            x => x.supplier
        );

    const scores =
        data.risk_analysis.map(
            x => x.score
        );

    new Chart(
        document.getElementById("riskChart"),
        {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Supplier Score",
                    data: scores
                }]
            }
        }
    );
}

loadData();