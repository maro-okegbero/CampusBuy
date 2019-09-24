var menu = document.getElementById('menu');
var nav = document.getElementById('nav');
var exit = document.getElementById('exit');


if (screen.width >= 1280 && screen.height >= 800){
    document.getElementsByTagName("body").innerHTML =
        "This website doesn't support Desktop mode, use your mobile phone :)"
}

menu.addEventListener('click', function(e){
    nav.classList.toggle('hide-mobile');
    e.preventDefault();
});
exit.addEventListener('click', function(e){
    nav.classList.add('hide-mobile');
});


//code for loading icon
// Wait for window load
	$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");;
	});


document.getElementById("demo").innerHTML =
"Screen Height: " + screen.height;

document.getElementById("demo").innerHTML =
"Screen Width: " + screen.width;


