window.onload = function() {
    var ball = document.querySelector('.landing-page-intro-content');
    
    ball.classList.add("landing-page-intro-content-animate");
    

};

window.onscroll = function () { 
    "use strict";
    var navbar = document.getElementById('navbar-container');
    var element = document.querySelector('.header-top');
    if (document.body.scrollTop >= 200 ) {
        navbar.classList.add("nav-colored");
    } 
    else {
        if(window.location.href.indexOf("blog") > -1) {
            var navbar = document.getElementById('navbar-container');
            navbar.classList.add("nav-colored");
            console.log("not-called")
     }
     else{navbar.classList.remove("nav-colored");}
        
    }
    
    if (document.body.scrollTop >= 450 ) {
        element.classList.add("hide");
    } 
    else {
        element.classList.remove("hide");
    }
};

function mask(){
    console.log("called")
    if(window.location.href.indexOf("blog") > -1) {
        var navbar = document.getElementById('navbar-container');
        navbar.classList.add("nav-colored");
        console.log("not-called")
 }
}

mask();

function preload() {
    myVar = setTimeout(showPage, 3000);
  }
  
function showPage() {
    document.getElementById("loader").style.display = "none";
    document.getElementById("myDiv").style.display = "block";
}


