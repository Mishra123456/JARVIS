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
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
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
});
