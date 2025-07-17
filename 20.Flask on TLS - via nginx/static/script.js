// ./static/script.js -->
document.addEventListener('DOMContentLoaded', onDOMContentLoaded);

function onDOMContentLoaded(event){
    startCamera();
    document.getElementById('snap').addEventListener('click', takePicture);
}

function startCamera(){
    navigator.mediaDevices.getUserMedia({video: true})
        .then(handleSuccess)
        .catch(handleError);
}

function handleSuccess(stream){
    const video = document.getElementById('video');
    video.srcObject = stream;
}

function handleError(err){
    console.error("カメラのアクセスに失敗しました:", err);
}

function takePicture(){
    const canvas = document.getElementById('canvas');
    const video = document.getElementById('video');
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
}