async function sendCommand(command) {
    let response = await fetch(`/api/${command}`);
    let responseText = await response.text();
    console.log(responseText);

    // Actually show the user on the screen
    document.querySelector("#responseText").innerHTML = responseText;
}


function main() {
    console.log("Ready!!!");

    document.querySelector("#ledon").onclick = () => {
        sendCommand("LED ON");
    };

    document.querySelector("#ledoff").onclick = () => {
        sendCommand("LED OFF");
    };

    document.querySelector("#flash").onclick = () => {
        let flashes = document.querySelector("#flashes").value;
        let periodms = document.querySelector("#periodms").value;
        sendCommand(`FLASH ${flashes} ${periodms}`);
    };
    
}

main();