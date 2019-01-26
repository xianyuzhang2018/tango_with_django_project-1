/*$(document).ready( function() {
    $("#about-btn").click( function(event) {
        alert("You clicked the button111 using JQuery!");
    });

    $(".ouch").click( function(event) {
        alert("You clicked1111 me! ouch!");
    });

    $("p").hover( function() {
    $(this).css('color', 'red');},
        function() {$(this).css('color', 'blue');});




});*/


$(document).ready( function() {
    $("#about-btn").addClass('btn btn-primary')

    $("#about-btn").click( function(event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + "ooo"
        $("#msg").html(msgstr)
});


});


