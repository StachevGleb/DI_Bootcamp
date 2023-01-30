let but = document.getElementById("lib-button")

but.addEventListener("click", clickListen)
function clickListen(e){
    e.preventDefault()
    let noun = document.getElementById("noun").value
    let adjective = document.getElementById("adjective").value
    let person = document.getElementById("person").value
    let verb = document.getElementById("verb").value
    let place = document.getElementById("place").value

    if(noun == "" || adjective == "" || person == "" || verb == "" || place == "") return
   
    let story = writeStory(noun, adjective, person, verb, place)
    console.log("story: ", story)
    append(story)
}

function append(story){
let par = document.getElementById("story")
let span = document.createElement("span")
span.textContent = story
par.appendChild(span)
}

function writeStory(noun, adjective, person, verb, place){
return `To look at ${noun}, think they are ${adjective}. My friend is ${person}.
We often ${verb}. I this ${place}`
}