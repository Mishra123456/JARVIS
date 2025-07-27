$(document).ready(function() {
  // For "SYSTEM CORE ONLINE" - Clear per-letter bounce
  $(".jarvis-text").textillate({
    in: { 
      effect: 'bounceIn',
      delayScale: 1.8,  // Slower delay between letters
      delay: 30,       // Increased per-letter delay
      shuffle: false,
      callback: function() {
        // Optional: Add echo effect after animation completes
        $(this).css('text-shadow', '0 0 10px #00f8ff');
      }
    },
    out: {
      effect: 'bounceOut',
      delayScale: 1.5,
      delay: 25,
      shuffle: false,
      sync: false      // Let letters fade out independently
    },
    loop: true,
    autoStart: true,
    minDisplayTime: 2000  // Show fully animated text for 2 seconds
  });
  
  // For "Ask me anything" - Clear staggered bounce
  $(".ask-me").textillate({
    in: { 
      effect: 'bounceInUp',
      delayScale: 2.0,  // Even more visible stagger
      delay: 40,       // Increased per-letter delay
      shuffle: false
    },
    out: {
      effect: 'bounceOutDown',
      delayScale: 1.8,
      delay: 35,
      shuffle: false,
      sync: false
    },
    loop: true,
    autoStart: true,
    initialDelay: 1500,  // Start after first animation begins
    minDisplayTime: 1500
  });
   // Siri configuration
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: window.innerWidth * 0.8, // Responsive width (80% of viewport)
    height: 150, // Reduced height for better mobile compatibility
    style: "ios9",
    amplitude: 1, // Changed from string to number
    speed: 0.3,   // Changed from string to number
    autostart: true,
    cover: true,  // Fills the container completely
    frequency: 2  // Smoother waves
});

// Handle window resize
window.addEventListener('resize', function() {
    siriWave.setWidth(window.innerWidth * 0.8);
});

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },
    });
    // 
    $("#MicBtn").click(function () { 
        eel.playassistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allcommands()();
    });

    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

      if (e.key === 'j' && e.metaKey) {
          eel.playassistantSound()
          $("#Oval").attr("hidden", true);
          $("#SiriWave").attr("hidden", false);
          eel.allcommands()();
      }
    }
    document.addEventListener('keyup', doc_keyUp, false);

     // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allcommands(message);//but allcommands has no paramter so we add one
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }
    }
    eel.expose(DisplayMessage); // <-- MUST BE PRESENT
    function DisplayMessage(message) {
      $('.siri-message').text(message);
}

     // toogle fucntion to hide and display mic and send button 
    eel.expose(ShowHideButton)
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }


    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    });
    
    // send button event handler
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    });

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });

});
