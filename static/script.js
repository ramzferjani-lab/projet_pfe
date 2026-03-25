function updateClock(){

let now = new Date()

document.getElementById("clock").innerHTML = now.toLocaleTimeString()

}

setInterval(updateClock,1000)

function clearFields(){

document.getElementById("user").value=""
document.getElementById("pass").value=""

}