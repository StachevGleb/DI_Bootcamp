// Exercise 1
let x = 5;
let y = 2;
if(x>y){
    console.log("x is the biggest number");
}else{
    console.log("y is the biggest number");
}

// Exercise 2
let newDog = 'Chihuahua';
let newDogLength = newDog.length;
console.log(newDogLength)
console.log(newDog.toLocaleLowerCase())
console.log(newDog.toLocaleUpperCase())
if(newDog == 'Chihuahua'){
    console.log("I love " + newDog + "s, it’s my favorite dog breed")
}else{
    console.log('I dont care, I prefer cats')
}

// Exercise 3
// let number = prompt("Tell me any number ?", "0 - 9")
// if(number%2 == 0){
//     console.log(number + " is an odd number")
// } else{
//     console.log(number + " is an even number")  
// }

// Exercise 4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000" ];
let usersLength = users.length;
console.log(usersLength)
console.log(typeof usersLength)


switch (usersLength) {
    // case 2:
    //     console.log(users[0] + ", " + users[1] + " " + "and " + (usersLength - 2) + " more are online")
    //     break;
    case 0:
        console.log("no one is online")
      break;
    case 1:
        console.log(users[0] + " is online")
        break;
    case 0:
       console.log(users[0] + " and " + users[1] + " " + "are online")
        break;
    default:
        console.log(users[0] + ", " + users[1] + " " + "and " + (usersLength - 2) + " more are online")
  }
 
