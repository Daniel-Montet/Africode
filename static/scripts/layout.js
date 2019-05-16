window.onload = function() {
    var ball = document.getElementById('ball');
    ball.style.marginLeft = "25px";
};

window.onscroll = function () { 
    "use strict";
    var navbar = document.getElementById('navbar');
    if (document.body.scrollTop >= 200 ) {
        navbar.classList.add("nav-colored");
        navbar.classList.remove("nav-transparent");
    } 
    else {
        navbar.classList.add("nav-transparent");
        navbar.classList.remove("nav-colored");
    }
};

