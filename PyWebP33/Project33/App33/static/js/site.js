document.addEventListener('DOMContentLoaded', () =>
{
    console.log('Script works');
});

const btn = document.getElementById('click');
const audio = new Audio(btn.getAttribute('data-sound'));
audio.preload = 'auto';

btn.addEventListener('mouseenter', () =>
{
    audio.currentTime = 0;
    audio.play();
});