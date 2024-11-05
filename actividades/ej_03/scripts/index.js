function read_temperature() {
    fetch(`/sensors/ds18b20/read`).then(response => response.json()).then(json => {
    
        document.querySelector("#temperature-value").innerText = json.temperature;
    });
}   

function send_setpoint() {
    let setpoint_value = parseInt(document.querySelector("#setpoint-slider").value);
    fetch(`/setpoint/set/${setpoint_value}`).then(response => response.json()).then(json => {
    
        document.querySelector("#buzzer-state").innerText = json.buzzer;
    });
}

// Function to update the setpoint display value
function updateSetpointValue(value) {
    document.getElementById("setpoint-value").innerText = value;
    send_setpoint();
}

setInterval(read_temperature, 500);