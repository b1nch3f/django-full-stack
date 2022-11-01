console.log('js from first_app');

$(document).ready(function(){
    $.get("/first_app/userdata", function(data, status){
        console.log("Data: " + JSON.parse(JSON.stringify(data)) + "\nStatus: " + status);
    })
});