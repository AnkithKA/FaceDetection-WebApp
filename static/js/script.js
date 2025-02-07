document.addEventListener("DOMContentLoaded", function(){
    console.log("Document loaded. Ready for further enhancements!");

    // Webcam capture elements
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('capture-btn');
    const submitWebcam = document.getElementById('submitWebcam');
    const imageDataInput = document.getElementById('image_data');

    // If the video element is present (i.e., in the Webcam tab)
    if (video) {
        // Request access to the webcam
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function(stream) {
                    video.srcObject = stream;
                    video.play();
                })
                .catch(function(err) {
                    console.error("Error accessing webcam: " + err);
                });
        }
        
        // When the "Capture" button is clicked:
        captureBtn.addEventListener("click", function() {
            // Set canvas dimensions to match video dimensions
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            // Draw the current video frame on the canvas
            const context = canvas.getContext('2d');
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            
            // Convert the canvas image to a data URL (base64)
            const dataURL = canvas.toDataURL('image/png');
            // Save the data URL in the hidden input field
            imageDataInput.value = dataURL;
            // Enable the submit button
            submitWebcam.disabled = false;
        });
    }
});
