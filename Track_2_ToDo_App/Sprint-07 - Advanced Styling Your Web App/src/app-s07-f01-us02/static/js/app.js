document.addEventListener("DOMContentLoaded", function() {
    const HIGHLIGHTEDITEM = 'highlighted-item';
    const currentPath = window.location.pathname;

    // Set the active tab based on the URL
    const setActiveTab = (tabId) => {
        const tabElement = document.getElementById(tabId);
        if (tabElement) {
            tabElement.classList.add('active');
        }
    };

    switch (true) {
        case currentPath.includes('/edit'):
            setActiveTab('edit-tab');
            break;
        case currentPath.includes('/completed'):
            setActiveTab('completed-tab');
            break;
        case currentPath.includes('/details'):
            setActiveTab('details-tab');
            break;
        case currentPath.includes('/recommend'):
            setActiveTab('recommendations-tab');
            break;
        default:
            break;
    }
    
    const highlightedItemId = localStorage.getItem(HIGHLIGHTEDITEM);
    console.log('highlightedItemId', highlightedItemId);
    if (highlightedItemId) {
        const highlightedItem = document.getElementById(highlightedItemId);
        if (highlightedItem) {
            highlightedItem.classList.add(HIGHLIGHTEDITEM);
        }
    }

    window.clearHighlight = function() {
        localStorage.removeItem(HIGHLIGHTEDITEM);
    };

    window.showDetails = function(li) {
        highlight(li);
        const rootUrl = window.location.origin;
        const dataId = li.getAttribute('data-id');
        window.location.href = `${rootUrl}/details/${dataId}`;
    };

    window.handleClick = function(event, cb) {
        event.stopPropagation();
        const rootUrl = window.location.origin;
        const cbId = cb.id;
        const cbChecked = cb.checked;
        window.location.href = `${rootUrl}/completed/${cbId}/${cbChecked}`;
        clearHighlight();
    };


    window.highlight = function(element) {
        const highlightedItemId = localStorage.getItem(HIGHLIGHTEDITEM);
        if (highlightedItemId) {
            const highlightedItem = document.getElementById(highlightedItemId);
            if (highlightedItem) {
                highlightedItem.classList.remove(HIGHLIGHTEDITEM);
            }
        }

        const closestListItem = element.closest('li');
        closestListItem.classList.add(HIGHLIGHTEDITEM);

        localStorage.setItem(HIGHLIGHTEDITEM, closestListItem.id);
    };


   //add javascript to support speech recognition for the todo input field
   const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
   const recognition = new SpeechRecognition();
   recognition.continuous = false;
   recognition.lang = "en-US";
   recognition.interimResults = false;

   window.captureVoice = function () {
       recognition.start();
       nameInput.value = "Your microphone is activated, speak to record voice";
   };

   recognition.onresult = function (event) {
       const transcript = event.results[0][0].transcript;
       const recognizedText = transcript.endsWith('.') ? transcript.slice(0, -1) : transcript;
       nameInput.value = recognizedText;
   };

   recognition.onspeechend = function () {
       recognition.stop();
   };

   recognition.onnomatch = function (event) {
       nameInput.value = "I didn't recognize that prompt.";
   };

   recognition.onerror = function (event) {
       nameInput.value = "Error occurred in recognition: " + event.error;
   };
});