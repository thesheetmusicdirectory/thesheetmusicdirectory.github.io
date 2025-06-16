// metronome-worker.js
let timerID = null;
let interval = 25; // Imposta l'intervallo predefinito a 25ms, che è il lookahead

self.onmessage = function(e) {
    if (e.data === 'stop') {
        clearInterval(timerID);
        timerID = null;
    } else if (e.data.interval) {
        interval = e.data.interval;
        // Se il timer è già in esecuzione, lo pulisce prima di impostarne uno nuovo
        if (timerID) {
            clearInterval(timerID);
        }
        timerID = setInterval(function() {
            postMessage('tick');
        }, interval);
    }
};