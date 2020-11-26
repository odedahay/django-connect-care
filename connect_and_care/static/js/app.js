document.addEventListener("DOMContentLoaded", function(event) {

// Hamburger menu //
const menuBtn = document.querySelector('.showMenu');
const closeBtn = document.querySelector('.closeMenu')
const show = document.getElementById('menu-content');
const contact = document.getElementById("contact-link");

// Programs clicks//
let navigationLink = document.querySelectorAll(".level");


menuBtn.addEventListener('click', showMenu);
closeBtn.addEventListener('click', closeMenu)



function showMenu(){
    show.style.right = "0";
    contact.classList.remove("contact-btn");
}

function closeMenu(){
    show.style.right = "-220px"
    contact.classList.add("contact-btn");
}


//navigationLink.forEach(menu => { menu.addEventListener('click', activatLink); })

 // Program scroll - activate the btn
// window.addEventListener('scroll', revealLink);

function activatLink(menu){
    const btnTarget = menu.currentTarget;
    //const level = btnTarget.dataset.level;
 
    // navigationLink.forEach(menulink => {
    //     menulink.classList.remove("active")
    // });

    // if we add new style in the body contents
    //document.querySelector("#" + level).classList.add('active');
    btnTarget.classList.add('active')
 }

 function revealLink(){
    //let navigationLink = document.querySelectorAll(".level");
    let fromTop = window.scrollY;

    navigationLink.forEach(link => {
        let section = document.querySelector(link.hash);

        if(section.offsetTop <= fromTop &&
           section.offsetTop + section.offsetHeight > fromTop
        ){
            link.classList.add('active')
        }else{
            link.classList.remove('active')
        }
    });
 }

 // FAQ Section
 var accordion = document.querySelectorAll('.accordion-button');
         
    for ( var i = 0; i < accordion.length; i++){
        accordion[i].addEventListener('click', function(){

            this.classList.toggle("active-display");

            var panel = this.nextElementSibling;
            
            if(panel.style.maxHeight){

                panel.style.maxHeight = null;
            }else{
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    }

});


// Footer Date
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();