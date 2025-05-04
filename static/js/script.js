document.addEventListener("DOMContentLoaded", function () {
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
                .then(function (stream) {
                    video.srcObject = stream;
                    video.play();
                })
                .catch(function (err) {
                    console.error("Error accessing webcam: " + err);
                });
        }

        // When the "Capture" button is clicked:
        captureBtn.addEventListener("click", function () {
            const context = canvas.getContext('2d');

            // Resize to smaller dimensions to reduce payload size
            const resizedWidth = 320;
            const resizedHeight = 240;

            canvas.width = resizedWidth;
            canvas.height = resizedHeight;

            // Draw the video frame scaled down
            context.drawImage(video, 0, 0, resizedWidth, resizedHeight);

            // Convert canvas to base64 string (JPEG is smaller than PNG)
            const dataURL = canvas.toDataURL('image/jpeg', 0.7); // 70% quality
            imageDataInput.value = dataURL;

            // Enable submit button
            submitWebcam.disabled = false;

            // Optional: Preview captured image
            const preview = document.getElementById("preview");
            if (preview) {
                preview.src = dataURL;
                preview.style.display = 'block';
            }
        });
    }
});
