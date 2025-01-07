// Video Player Script

const videoPlayer = document.getElementById('video-player');
const videoSource = document.getElementById('video-source');

// Video event listeners
videoPlayer.addEventListener('play', onVideoPlay);
videoPlayer.addEventListener('pause', onVideoPause);
videoPlayer.addEventListener('ended', onVideoEnded);

// Upload Form Script

const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');

uploadForm.addEventListener('submit', handleUploadSubmit);

// Index Page Script

const indexPage = document.getElementById('index-page');
const videoList = document.getElementById('video-list');

fetchVideos();

// Custom JavaScript functions

// Play video function
function playVideo(videoId) {
    const video = document.getElementById(`video-${videoId}`);
    video.play();
    console.log(`Playing video ${videoId}`);
}

// Pause video function
function pauseVideo(videoId) {
    const video = document.getElementById(`video-${videoId}`);
    video.pause();
    console.log(`Pausing video ${videoId}`);
}

// Stop video function
function stopVideo(videoId) {
    const video = document.getElementById(`video-${videoId}`);
    video.pause();
    video.currentTime = 0;
    console.log(`Stopping video ${videoId}`);
}

// Mute video function
function muteVideo(videoId) {
    const video = document.getElementById(`video-${videoId}`);
    video.muted = true;
    console.log(`Muting video ${videoId}`);
}

// Unmute video function
function unmuteVideo(videoId) {
    const video = document.getElementById(`video-${videoId}`);
    video.muted = false;
    console.log(`Unmuting video ${videoId}`);
}

// Fullscreen video function
function fullscreenVideo(videoId) {
    const video = document.getElementById(`video-${videoId}`);
    video.requestFullscreen();
    console.log(`Fullscreen video ${videoId}`);
}

// Event handler functions

function onVideoPlay() {
    console.log('Video playing');
}

function onVideoPause() {
    console.log('Video paused');
}

function onVideoEnded() {
    console.log('Video ended');
}

function handleUploadSubmit(e) {
    e.preventDefault();
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
}

function fetchVideos() {
    fetch('/videos')
    .then((response) => response.json())
    .then((data) => {
        const videos = data.videos;
        videos.forEach((video) => {
            const videoElement = document.createElement('li');
            videoElement.innerHTML = `
                <a href="/play/${video.id}">${video.title}</a>
            `;
            videoList.appendChild(videoElement);
        });
    })
    .catch((error) => console.error(error));
}