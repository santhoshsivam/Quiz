var set_minutes = 15;
let time = 15 * 60;
let obj = document.getElementById("cookie");
let change = document.getElementById('demo');
let cookie = readcookie();
if (cookie[0] == true) {
    time = cookie[1];
}


setInterval(countdown, 1000);

function countdown() {


    const count = Math.floor(time / 60);
    var seconds = time % 60;
    if ((time % 60) == 0) {
        seconds = seconds + '0';
    }
    if (seconds > 0 && seconds < 10) {
        seconds = '0' + seconds;
    }
    countsecond = count + ":" + seconds;
    obj.value = time;
    change.innerHTML = countsecond;
    time--;
    return countsecond;

}

function setcookie() {
    var time = countdown();
    document.cookie = "Time11=" + time;
}

function readcookie() {

    let found = document.cookie;

    var b = found.split('=');
    let f = b[0];
    if (f == "Time11") {
        var c = b[1].split(';');
        var d = c[0].split(':');
        let e = parseInt(d[0]);
        let g = parseInt(d[1]);
        var h = (e * 60) + g;
        return [true, h];

    }
    return false;
}