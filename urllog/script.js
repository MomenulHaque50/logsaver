document.addEventListener('DOMContentLoaded', function () {
    const socket = io();

    const logList = document.getElementById('logList');

    socket.on('log_entry', function (logEntry) {
        const listItem = document.createElement('li');
        listItem.textContent = `${logEntry.timestamp} - Source: ${logEntry.src_ip}, Destination: ${logEntry.dst_ip}`;
        logList.appendChild(listItem);
    });
});
