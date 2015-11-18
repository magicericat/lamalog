"use strict";
$(document).ready(function () {
    var button = $("#startRecording")
    $("#startRecording").click(function() {
        console.log("anything")
        var port = $("#eegPort").val();
        console.log(port)
        var portNumber = {"port": port}
        $.post("/collectdata",
                portNumber,
                function(data) {
                        //show button to move on to results page
                        $("#showResults").show()
                        console.log("anything")
                        console.log(data)
                        //<button id="button-id" class="btn btn-default" style="display:none">Text of button</button>
        });
        //start timer

    });
 });