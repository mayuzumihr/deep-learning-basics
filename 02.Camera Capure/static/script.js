document.addEventListener('DOMContentLoaded', onDOMContentLoaded);

function onDOMContentLoaded(event) {
    startCamera();
    document.getElementById('snap').addEventListener('click', takePicture);
}

function startCamera() {
    navigator.mediaDevices.getUserMedia({video: true})
        .then(handleSuccess)
        .catch(handleError);
}

function handleSuccess(stream) {
    const video = document.getElementById('video');
    video.srcObject = stream;
}

function handleError(err) {
    console.error("カメラのアクセスに失敗しました:", err);
}

function takePicture() {
    const canvas = document.getElementById('canvas');
    const video = document.getElementById('video');
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(processBlob);
}

function processBlob(blob) {
    const file = new File([blob], 'snapshot.png', {type: 'image/png'});
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    document.getElementById('file').files = dataTransfer.files;
//    document.getElementById('uploadForm').submit();
}