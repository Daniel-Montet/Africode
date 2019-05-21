window.onload = function() {
    var ball = document.querySelector('.landing-page-intro-content');
    // ball.style.marginTop = "-100px";
    console.log(ball);
    ball.classList.add("landing-page-intro-content-animate");
};

window.onscroll = function () { 
    "use strict";
    var navbar = document.getElementById('navbar-container');
    if (document.body.scrollTop >= 200 ) {
        navbar.classList.add("nav-colored");
    } 
    else {
        navbar.classList.remove("nav-colored");
    }
};

