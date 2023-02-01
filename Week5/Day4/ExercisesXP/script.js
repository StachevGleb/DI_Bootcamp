// Exercise 1
// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

// function helloW(){
//     alert("hello world")
// }
// setTimeout(helloW, 2000)

// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

// function pTagAdding(){
//    let par = document.createElement("p")
//    let text0 = document.createTextNode("hello world")
//    par.appendChild(text0)
//    let div0 = document.getElementById("container")
//    div0.appendChild(par)
// }
// setTimeout(pTagAdding, 2000)

// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

// let clrInt = setInterval(pTagAdding, 2000)
// let clr = document.querySelector("#clear")
// function myStopFunction() {
//     clearInterval(clrInt);
//   } 
// clr.addEventListener("click", myStopFunction) 
// setTimeout(function(){clearInterval(clrInt)}, 10000)

// Exercise 2
// In your Javascript file, use setInterval to move the <div id="animate"> 
// to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it 
// reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions

// let but = document.getElementById("but")
// let div1 = document.getElementById("containero")
// let div2 = document.getElementById("animate")
// let distance = 0
// let inter=0
// function moveLeftEl(){
//     if(distance === 350) {
//      clearInterval(inter)
//         return
//     }
//     distance += 1
//     div2.style.marginLeft = distance + "px"
// }
// function myMove(){
//   inter =  setInterval(moveLeftEl, 1)
// }

// Exercise 3
let dropBox = document.getElementById("target")
let dragBox = document.getElementById("box")

function dragStart(ev){
}
function allowDrop(ev){
    ev.preventDefault()
    dropBox.classList.add("is-hovered")
}
function drop(ev){
    ev.preventDefault
    dropBox.appendChild(dragBox)
}
function dragEnter(ev){
}
function dragLeave(ev){
    dropBox.classList.remove("is-hovered")
    // dropBox.style.border = "none"
}

 
    
 

