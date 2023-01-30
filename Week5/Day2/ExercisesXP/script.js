// // Exercise 1 
// let hTag = document.querySelector("h1")
// console.log(hTag)
// let lastChild = document.querySelector("article")
// lastChild.lastElementChild.remove()
// console.log(lastChild)
// let hTwo = document.getElementById("hTwo")
// console.log(hTwo)
// hTwo.addEventListener("click", function() {
//     hTwo.setAttribute("style", "backGround-color: red")
//   })
// let hThree = document.getElementById("hThree")
// hThree.addEventListener("click", function() {
//     hThree.setAttribute("style","display: none")
// })
// let but = document.createElement("button")
// let cont = document.createTextNode("bold but")
// but.appendChild(cont)
// document.body.appendChild(but)
// let pars = document.querySelectorAll("p")
// console.log(pars.length)
// but.addEventListener("click", function(){
// for(let i = 0; i < pars.length; i++){
//     pars[i].setAttribute("style", "font-weight: bold")
// }
// })

// // Exercise 2
// let form = document.getElementById("fr")
// console.log(form)
// // let sub = document.getElementById("submit")
// console.log(form, fname, lname)
// form.addEventListener("submit", function(e){
//     e.preventDefault()
//     let fname = document.querySelector("[name=fname]").value
//     let lname = document.getElementById("lname").value    
//     console.log(fname, lname)
//     if(fname === "" || lname === ""){
//         console.log("not field")
//     }else{
//         let ul = document.querySelector(".usersAnswer")
//         ul.innerHTML = ""
//         let li1 = document.createElement("li")
//         let li2 = document.createElement("li")
//         li1.textContent = fname
//         li2.innerHTML = lname
//         ul.append(li1, li2)
//     }
// })

// // Exercise 3

// // Declare a global variable named allBoldItems.

// let allBoldItems 

// // Create a function called getBold_items() that takes no parameter. 
// // This function should collect all the bold items inside the paragraph and assign 
// // them to the allBoldItems variable.
// function getBoldItems() {
//     allBoldItems = document.getElementsByTagName("strong")
// }
// // Create a function called highlight() that changes the color of all the bold text to blue.
// function highlight(){
//     getBoldItems()
//     for(let i = 0; i < allBoldItems.length;i++){
//         allBoldItems[i].setAttribute("style", "color: blue")
//     }
// }
// // highlight()
// // Create a function called return_normal() that changes the color of all the bold text back to black.
// function returnNormal(){
//     getBoldItems()
//     for(let boldItem of allBoldItems){
//     boldItem.style.color = "black"
//     }
// }
// // Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph)
// //  and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
// let par = document.querySelector("p")
// par.addEventListener("mouseover", highlight)
// par.addEventListener("mouseout", returnNormal)

// // Exercise 4
// let form = document.getElementById("MyForm")
// let radius = document.getElementById("radius")
// form.addEventListener("submit", toCalculate)
// let v = document.getElementById("volume")

// function toCalculate(e){
//     e.preventDefault()
// let a = (radius.value)
// if(Number.isNaN(a)){
//     return
// }
// let v = (4/3) * Math.PI * a ** 3 
// console.log("result: ", volume)
// volume.value = v
// }

// Exercise 5
document.addEventListener("DOMContentLoaded", contentLoaded)
function contentLoaded(){
console.log("HTML loaded")
}
