let names= ["john", "sarah", 23, "Rudolf",34]
let i;
let character;
// console.log(typeof names[1])
for(i=0;i<names.length;i++){
if(typeof names[i] != "string"){
continue
} else if (names[i].toUpperCase() != names[i]) {
    console.log(names[i][0].toUpperCase() + names[i])
}
}