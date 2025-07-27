//used for connection of frontend with python using else
    //now we want works.py to get used here
//i.e jab bhi mic pe click hoga ye speech wala on ho jaayega

// to ensure ki jab recognie ho toh bole ya listening ho toh bole
 $(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }
    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

});
