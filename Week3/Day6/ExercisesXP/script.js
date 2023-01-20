// Exercise 1 

// Part I
// const people = ["Greg", "Mary", "Devon", "James"];
// people.shift()
// console.log(people)
// people.splice(people.indexOf("James"), 1, "Jason")
// console.log(people)
// people.push("Gleb")
// console.log(people)
// console.log(people.indexOf("Mary"))
// let newPeople = people.slice(1,3)
// console.log(newPeople)
// console.log(people.indexOf("Foo"))
// // because this item not exists
// let last = newPeople[newPeople.length-1];
// console.log(last)

// // Part II
// // for(let i = 0; i < people.length-1; i++){
// //     console.log(people[i])
// // }

// for(let i = 0; i < people.length-1; i++){
//    if(people[i] == "Jason"){
//     break
//    }
//     console.log(people[i])
// }

// // Exercise 2

// let colors = ["red", "blue", "green"];
// let suffixes = ["1st", "2nd", "3rd"];
// for(let i = 0; i < colors.length;i++){
// console.log("My "+suffixes[i]+" choice is " + colors[i])
// }

// // Exercise 3

// let num = prompt("Insert number, please ... ", "from 10 to infinity");
// while(num < 10){
// num = prompt("Insert number, please ... ","must be greater than 10")
// }

// // Exercise 4
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }
// console.log("number of floors in the building = ", building.numberOfFloors);
// console.log("how many apartments are on the floors 1 and 3 = ", building.numberOfAptByFloor.firstFloor," and " ,building.numberOfAptByFloor.thirdFloor)
// console.log("name of the second tenant and the number of rooms he has in his apartment = ", building.nameOfTenants[1], " and ", building.numberOfRoomsAndRent.dan[0])
// if((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]){
// building.numberOfRoomsAndRent.dan[1] = building.numberOfRoomsAndRent.dan[1] + 1200
// console.log("Dan new flat rent price = ", building.numberOfRoomsAndRent.dan[1])
// }

// // Exercise 5 

// let family = {
//     Yosi: "son",
//     Sara: "mother",
//     Alex: "father"
// }

// for(let fam in family){
//     console.log("keys = ", fam)
//     console.log("values = ", family[fam])
// }

// // Exercise 6

// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   }
// let str = ""; 
//  for(let i in details){
//     str = str + " " + i + " " + details[i]  
//  }
//  console.log(str)

// Exercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let letter = [];
for(let i = 0; i < names.length;i++){
   letter.push(names[i][0])
}
// console.log(letter)
// console.log(letter.sort())
letter.sort()
let a = letter.join("")
console.log(a)