function controlLED(led) {
    fetch(`/led/toggle/${led}`);
}

function controlRGB() {
    let red = document.querySelector("#redRange").value;
    let blue = document.querySelector("#blueRange").value;
    let green = document.querySelector("#greenRange").value;
    fetch(`/rgbled/change/red/${red}`);
    fetch(`/rgbled/change/blue/${blue}`);
    fetch(`/rgbled/change/green/${green}`);
}