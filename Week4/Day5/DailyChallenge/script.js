let planets = [
    {name: Earth, moons: 1},
    {name: Mars, moons: 0},
    {name: Jupiter, moons: 0},
    {name: Saturn, moons: 0},
    {name: Uranus, moons: 0},
    {name: Neptune, moons: 0},
]

for(let planet of planets){
let div = document.createElement("div")
div.classList.add("planet")
div.classList.add(planet.name.toLowerCase())
for(let i = 0; i < planet.moons;i++){
    let moonDiv = document.createElement("div")
    moonDiv.classList.add("moon")
    div.appendChild(moonDiv)
}
let section = document.querySelector(".listPlanets")
section.appendChild("div")
}