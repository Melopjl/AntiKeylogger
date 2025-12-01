function loadProcesses() {
    fetch("/processes")
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("process-table");
            const count = document.getElementById("process-count");
            if (!data.processes) return;

            table.innerHTML = "";
            count.innerText = data.processes.length;

            data.processes.forEach(proc => {
                const row = document.createElement("tr");
                const pidCell = document.createElement("td");
                const nameCell = document.createElement("td");

                pidCell.innerText = proc.pid;
                nameCell.innerText = proc.name;

                row.appendChild(pidCell);
                row.appendChild(nameCell);
                table.appendChild(row);
            });
        });
}

// Atualiza logs
function loadLogs() {
    fetch("/logs")
        .then(res => res.json())
        .then(data => {
            const logBox = document.getElementById("log-box");
            if (logBox && data.logs) logBox.innerText = data.logs;
        });
}

// Intervalos de atualização
setInterval(loadProcesses, 5000);
setInterval(loadLogs, 5000);

// Botão scan animação
document.addEventListener("DOMContentLoaded", () => {
    const scanBtn = document.getElementById("scan-btn");
    if (scanBtn) {
        scanBtn.addEventListener("click", () => {
            scanBtn.classList.add("btn-click");
            setTimeout(() => scanBtn.classList.remove("btn-click"), 150);
        });
    }
});
