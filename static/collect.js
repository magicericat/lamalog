"use strict";
$(document).ready(function () {
    var button = $("#startRecording")
    $("#startRecording").click(function() {
        var timer = new Tock({
                callback: function () {
                    $('#clockface').val(timer.msToTime(timer.lap()));
                }
            });

        var countdown = Tock({
                countdown: true,
                interval: 10,
                callback: function () {
                    console.log(countdown.lap() / 1000);
                    $('#countdown_clock').val(timer.msToTime(countdown.lap()));
                },
                complete: function () {
                    console.log('end');
                    alert("Time's up!");
                }
            });
        countdown.start($('#countdown_clock').val());
        //start timer
        $("#countdown").show()
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

    });
 });