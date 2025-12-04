document.addEventListener('DOMContentLoaded', () =>
{
    console.log('Script works');
    let btn = document.getElementById("btn-seed");
    if (btn)
    {
        btn.addEventListener('click', btnSeedClick);
    }
});

//const btn = document.getElementById('click');
//const audio = new Audio(btn.getAttribute('data-sound'));
//audio.preload = 'auto';
//
//btn.addEventListener('mouseenter', () =>
//{
//    audio.currentTime = 0;
//    audio.play();
//});

function btnSeedClick()
{
    if (confirm("Its very danger. Confirm?"))
    {
        fetch("/seed/",
        {
            method: "PATCH"
        }).then(r => r.json())
        .then(j =>
        {
            console.log(j);
        });
    }
}