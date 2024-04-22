document.addEventListener("DOMContentLoaded", function() {
    const nameInput = document.getElementById("todo");
    
    //add javascript to support speech recognition for the todo input field
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = "en-US";
    recognition.interimResults = false;
    
    window.captureVoice = function() {
        recognition.start();
        nameInput.value = "Your microphone is activated, speak to record voice";
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        const recognizedText = transcript.endsWith('.') ? transcript.slice(0, -1) : transcript;
        nameInput.value = recognizedText;
    };

    recognition.onspeechend = function() {
        recognition.stop();
    };

    recognition.onnomatch = function(event) {
        nameInput.value = "I didn't recognize that prompt.";
    };

    recognition.onerror = function(event) {
        nameInput.value = "Error occurred in recognition: " + event.error;
    };
});