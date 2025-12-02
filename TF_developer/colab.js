// STEPS : 
    // 1. execute this : console> allow pasting 
    // 2. past the ConnectButton() function and Enter
    // 3. past the next line and Enter

function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}


var colab = setInterval(ConnectButton,60000);
// 60,000 => 60 Seconds



// clearInterval(colab)