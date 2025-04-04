async function sendCommand(command) {
    let response = await fetch(`/api/${command}`);
    let responseText = await response.text();
    console.log(responseText);

    // Actually show the user on the screen
    document.querySelector("#responseText").innerHTML = responseText;
}


function main() {
    console.log("Ready!!!");

    document.querySelector("#reset").onclick = () => {
        console.log("Resetting...");
        sendCommand("RESET");
    };

    document.querySelector("#x1").onclick = () => {
        sendCommand("X-AXIS 1");
    };

    document.querySelector("#x2").onclick = () => {
        sendCommand("X-AXIS 2");
    };

    document.querySelector("#x3").onclick = () => {
        sendCommand("X-AXIS 3");
    };

    document.querySelector("#x4").onclick = () => {
        sendCommand("X-AXIS 4");
    };

    document.querySelector("#x5").onclick = () => {
        sendCommand("X-AXIS 5");
    };

    document.querySelector("#zextend").onclick = () => {
        sendCommand("Z-AXIS EXTEND");
    };

    document.querySelector("#zretract").onclick = () => {
        sendCommand("Z-AXIS RETRACT");
    };

    document.querySelector("#gripperopen").onclick = () => {
        sendCommand("GRIPPER OPEN");
    };

    document.querySelector("#gripperclose").onclick = () => {
        sendCommand("GRIPPER CLOSE");
    };

    document.querySelector("#loaderstatus").onclick = () => {
        sendCommand("LOADER_STATUS");
    };

    document.querySelector("#move").onclick = () => {
        let fromIndex = document.querySelector("#fromIndex").value;
        let toIndex = document.querySelector("#toIndex").value;
        sendCommand(`MOVE ${fromIndex} ${toIndex}`);
    };
    
}

main();