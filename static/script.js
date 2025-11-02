async function fetchData() {
    const res = await fetch('/data');
    const builds = await res.json();
    displayData(builds);
}

async function detectAnomalies() {
    const res = await fetch('/detect');
    const builds = await res.json();
    displayData(builds);let autoRefresh = false;
let intervalId = null;

async function fetchData() {
    const res = await fetch('/data');
    const builds = await res.json();
    displayData(builds);
}

async function detectAnomalies() {
    const res = await fetch('/detect');
    const builds = await res.json();
    displayData(builds);
}

function displayData(builds) {
    const tbody = document.querySelector('#buildTable tbody');
    tbody.innerHTML = '';

    builds.forEach(b => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${b.build_id}</td>
            <td>${b.duration}</td>
            <td>${b.status}</td>
            <td class="${b.anomaly ? 'anomaly' : ''}">
                ${b.anomaly ? '⚠️ Anomaly' : '✅ Normal'}
            </td>
        `;
        tbody.appendChild(row);
    });
}

function toggleAutoRefresh() {
    const statusLabel = document.getElementById('statusLabel');
    const toggleBtn = document.getElementById('toggleBtn');

    autoRefresh = !autoRefresh;
    if (autoRefresh) {
        toggleBtn.textContent = "Stop Auto Refresh";
        statusLabel.textContent = "🔄 Auto refresh: ON";
        intervalId = setInterval(detectAnomalies, 5000); // every 5 sec
        detectAnomalies(); // immediate run
    } else {
        toggleBtn.textContent = "Start Auto Refresh";
        statusLabel.textContent = "⏸️ Auto refresh: OFF";
        clearInterval(intervalId);
    }
}

}

function displayData(builds) {
    const tbody = document.querySelector('#buildTable tbody');
    tbody.innerHTML = '';

    builds.forEach(b => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${b.build_id}</td>
            <td>${b.duration}</td>
            <td>${b.status}</td>
            <td class="${b.anomaly ? 'anomaly' : ''}">
                ${b.anomaly ? '⚠️ Anomaly' : 'Normal'}
            </td>
        `;
        tbody.appendChild(row);
    });
}
